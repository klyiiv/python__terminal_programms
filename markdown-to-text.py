'''markdown to text / yandex.lyceum project d4k07 /  21 april 2021'''
from abc import ABCMeta, abstractmethod
import re

class Utils():
    
    @classmethod
    def getBlocksFile(cls,text):
        def blocks():
            block   = []
            for line in open(text,'r').readlines():
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block).strip()
                    block   = []
        return list(blocks())
    
    @classmethod
    def getBlocksString(cls,text):
        def blocks():
            block   = []
            for line in text.split("\n"):
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block)
                    block   = []
        return list(blocks())
    
    @classmethod
    def output(cls,content):
        with open('output/output.html','w') as f:
            f.write(content)
        assert(f.closed)

class Handler():
    def callback(self,prefix, name, *args):
        # вызывает метод когда придут аргументы 
        method = getattr(self,prefix+name,None) # find method
        try:    return method(*args)
        # при ошибке вернуть none
        except: return None
        
    def start(self, name):
        return self.callback('start_',name)
    
    def end(self,name):

        return self.callback('end_', name)
    
    def sub(self,name):
        def substitution(match):
            result  = self.callback('sub_',name,match)
            if result is None: 
                result = match.group(0)
            return result
        return substitution
    
class HTMLRenderer(Handler):
    
    # html document rules
    def start_document(self):
        """
        @return: basic start of HTML document
        """
        return '<html><head><title></title></head><body>'
    
    def end_document(self):
        return '</body></html>'

    # paragraph rules
    def start_paragraph(self):
        return '<p>'
    
    def end_paragraph(self):
        return '</p>'
    
    # heading rules
    def start_heading(self):
        return '<h1>'
    
    def end_heading(self):
        return '</h1>'
    
    # substitutions
    def sub_strong(self,match):
        return '<strong>{0}</strong>'.format(match.group(1))

    # Break rules
    def sub_break(self,match):
        return '<br />'
    
    def data(self,block):
        return block
    
    
class Rule(metaclass=ABCMeta):

        """
        У правила есть условие, действие и тип.
        Если условие выполнено, действие будет применено.
        Каждое правило должно иметь тип, объясняющий его назначение
        отсутствие типа означает, что нет правила, которое нужно выполнить
        """

    def action(self, block, handler):
        """
        @return: String - block with rule applied or Boolean - NA
            Action should be the same for all rules
        """
        if self._type:
            return ''.join([handler.start(self._type),handler.data(block),handler.end(self._type)])
        return False
    
    @abstractmethod
    def condition(self,block):
    
        return False
        
    def type(self):

        return self._type
    
class HeadingRule(Rule):

    _type = "heading"
    
    def condition(self,block):
        return (('\n' not in block) and (len(block)<=70))
    
class ParagraphRule(Rule):
    
    _type = "paragraph"
    
    def condition(self, block):
        return True
    
class Parser(object):
    '''
    classdocs
    '''
    def __init__(self,handler):
        
        self._handler   = handler
        self._rules     = []
        self._filters   = []
        
    @property
    def handler(self):
        return self._handler
    
    @property
    def rules(self):
        return self._rules
    
    def add_rule(self, *args):
        """
        Порядок добавления правил ВАЖЕН
        """
        for rule in args:
            self._rules.append(rule)
    
    @property
    def filters(self):
        return self._filters
    
    def add_filter(self, pattern, name):
        
        def apply_filter(block,handler):
            
            return re.sub(pattern,handler.sub(name),block)
        self._filters.append(apply_filter)
        
    def parse(self,content):
    
        def parse_help():
            yield self.handler.start("document")
            for block in Utils.getBlocksFile(content):
                for filter_meth in self.filters: 
                    block   = filter_meth(block,self.handler)
                for rule in self._rules:
                    if rule.condition(block):
                        
                        action  = rule.action(block,self._handler)
                        
                        if action:
                            yield action
                        break;
                    
            yield self.handler.end("document")
            
        return "".join([x for x in parse_help() if isinstance(x,str)])
    

    
if __name__ == "__main__":
    y       = HTMLRenderer()
    x       = Parser(y)
    f       = "../test_resources/markup_text.txt"
    x.add_rule(HeadingRule(),ParagraphRule())
    x.add_filter(r"\*(.+|.?)\*", 'strong')
    x.add_filter(r"*  \n",'break',)
    t       = x.parse(f)
    Utils.output(t)
    
