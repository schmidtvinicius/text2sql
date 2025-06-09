# Generated from text2sql/cfg/parser/text2sql.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .text2sqlParser import text2sqlParser
else:
    from text2sqlParser import text2sqlParser

# This class defines a complete listener for a parse tree produced by text2sqlParser.
class text2sqlListener(ParseTreeListener):

    # Enter a parse tree produced by text2sqlParser#prog.
    def enterProg(self, ctx:text2sqlParser.ProgContext):
        print('SELECT ', end='')
        if ctx.columnList() is None and ctx.aggregator() is None:
            print('* ', end='')
        if ctx.ordering():
            print('FROM ', end='')
            if type(ctx.table().getChild(0)).__name__ == 'VulnerabilityContext':
                print('vulnerability', end=' ')

    # Exit a parse tree produced by text2sqlParser#prog.
    def exitProg(self, ctx:text2sqlParser.ProgContext):
        print(';')


    # Enter a parse tree produced by text2sqlParser#table.
    def enterTable(self, ctx:text2sqlParser.TableContext):
        if ctx.parentCtx.ordering() is None:
            print('FROM ', end='')

    # Exit a parse tree produced by text2sqlParser#table.
    def exitTable(self, ctx:text2sqlParser.TableContext):
        pass


    # Enter a parse tree produced by text2sqlParser#columnList.
    def enterColumnList(self, ctx:text2sqlParser.ColumnListContext):
        pass

    # Exit a parse tree produced by text2sqlParser#columnList.
    def exitColumnList(self, ctx:text2sqlParser.ColumnListContext):
        if ctx.parentCtx.table() is None:
            print('FROM vulnerability ', end='')


    # Enter a parse tree produced by text2sqlParser#vulnerability.
    def enterVulnerability(self, ctx:text2sqlParser.VulnerabilityContext):
        if ctx.parentCtx.parentCtx.ordering() is None:
            print('vulnerability ', end='')

    # Exit a parse tree produced by text2sqlParser#vulnerability.
    def exitVulnerability(self, ctx:text2sqlParser.VulnerabilityContext):
        pass


    # Enter a parse tree produced by text2sqlParser#aggregator.
    def enterAggregator(self, ctx:text2sqlParser.AggregatorContext):
        pass

    # Exit a parse tree produced by text2sqlParser#aggregator.
    def exitAggregator(self, ctx:text2sqlParser.AggregatorContext):
        pass


    # Enter a parse tree produced by text2sqlParser#max.
    def enterMax(self, ctx:text2sqlParser.MaxContext):
        print('MAX(', end='')

    # Exit a parse tree produced by text2sqlParser#max.
    def exitMax(self, ctx:text2sqlParser.MaxContext):
        pass


    # Enter a parse tree produced by text2sqlParser#min.
    def enterMin(self, ctx:text2sqlParser.MinContext):
        print('MIN(', end='')

    # Exit a parse tree produced by text2sqlParser#min.
    def exitMin(self, ctx:text2sqlParser.MinContext):
        pass


    # Enter a parse tree produced by text2sqlParser#avg.
    def enterAvg(self, ctx:text2sqlParser.AvgContext):
        print('AVG(', end='')

    # Exit a parse tree produced by text2sqlParser#avg.
    def exitAvg(self, ctx:text2sqlParser.AvgContext):
        pass


    # Enter a parse tree produced by text2sqlParser#column.
    def enterColumn(self, ctx:text2sqlParser.ColumnContext):
        pass

    # Exit a parse tree produced by text2sqlParser#column.
    def exitColumn(self, ctx:text2sqlParser.ColumnContext):
        if type(ctx.parentCtx).__name__ == 'ColumnListContext':
            last_column = ctx.parentCtx.getChild(ctx.parentCtx.getChildCount() - 1)
            if last_column != ctx.getRuleContext():
                print(', ', end='')
        if hasattr(ctx.parentCtx, 'aggregator') and ctx.parentCtx.aggregator() is not None:
            print(') FROM vulnerability', end='')


    # Enter a parse tree produced by text2sqlParser#cve.
    def enterCve(self, ctx:text2sqlParser.CveContext):
        print('cve ', end='')

    # Exit a parse tree produced by text2sqlParser#cve.
    def exitCve(self, ctx:text2sqlParser.CveContext):
        pass


    # Enter a parse tree produced by text2sqlParser#title.
    def enterTitle(self, ctx:text2sqlParser.TitleContext):
        print('title ', end='')

    # Exit a parse tree produced by text2sqlParser#title.
    def exitTitle(self, ctx:text2sqlParser.TitleContext):
        pass


    # Enter a parse tree produced by text2sqlParser#confidence.
    def enterConfidence(self, ctx:text2sqlParser.ConfidenceContext):
        print('confidence ', end='')

    # Exit a parse tree produced by text2sqlParser#confidence.
    def exitConfidence(self, ctx:text2sqlParser.ConfidenceContext):
        pass


    # Enter a parse tree produced by text2sqlParser#severity.
    def enterSeverity(self, ctx:text2sqlParser.SeverityContext):
        print('severity ', end='')

    # Exit a parse tree produced by text2sqlParser#severity.
    def exitSeverity(self, ctx:text2sqlParser.SeverityContext):
        pass


    # Enter a parse tree produced by text2sqlParser#cvss.
    def enterCvss(self, ctx:text2sqlParser.CvssContext):
        print('cvss ', end='')

    # Exit a parse tree produced by text2sqlParser#cvss.
    def exitCvss(self, ctx:text2sqlParser.CvssContext):
        pass


    # Enter a parse tree produced by text2sqlParser#epss.
    def enterEpss(self, ctx:text2sqlParser.EpssContext):
        print('epss ', end='')

    # Exit a parse tree produced by text2sqlParser#epss.
    def exitEpss(self, ctx:text2sqlParser.EpssContext):
        pass


    # Enter a parse tree produced by text2sqlParser#age.
    def enterAge(self, ctx:text2sqlParser.AgeContext):
        print('age', end='')

    # Exit a parse tree produced by text2sqlParser#age.
    def exitAge(self, ctx:text2sqlParser.AgeContext):
        pass


    # Enter a parse tree produced by text2sqlParser#cwe.
    def enterCwe(self, ctx:text2sqlParser.CweContext):
        print('cwe ', end='')

    # Exit a parse tree produced by text2sqlParser#cwe.
    def exitCwe(self, ctx:text2sqlParser.CweContext):
        pass


    # Enter a parse tree produced by text2sqlParser#kev.
    def enterKev(self, ctx:text2sqlParser.KevContext):
        print('kev ', end='')

    # Exit a parse tree produced by text2sqlParser#kev.
    def exitKev(self, ctx:text2sqlParser.KevContext):
        pass


    # Enter a parse tree produced by text2sqlParser#comparison.
    def enterComparison(self, ctx:text2sqlParser.ComparisonContext):
        print('WHERE ', end='')

    # Exit a parse tree produced by text2sqlParser#comparison.
    def exitComparison(self, ctx:text2sqlParser.ComparisonContext):
        pass


    # Enter a parse tree produced by text2sqlParser#number_comparison.
    def enterNumber_comparison(self, ctx:text2sqlParser.Number_comparisonContext):
        if type(ctx.getChild(0)).__name__ == 'TerminalNodeImpl':
            print(ctx.getChild(0).getText(), end='')

    # Exit a parse tree produced by text2sqlParser#number_comparison.
    def exitNumber_comparison(self, ctx:text2sqlParser.Number_comparisonContext):
        if type(ctx.getChild(ctx.getChildCount() - 1)).__name__ == 'TerminalNodeImpl':
            print(ctx.getChild(ctx.getChildCount() - 1).getText(), end='')


    # Enter a parse tree produced by text2sqlParser#bool_comparison.
    def enterBool_comparison(self, ctx:text2sqlParser.Bool_comparisonContext):
        pass

    # Exit a parse tree produced by text2sqlParser#bool_comparison.
    def exitBool_comparison(self, ctx:text2sqlParser.Bool_comparisonContext):
        if ctx.bool_() is None:
            print('= 1')


    # Enter a parse tree produced by text2sqlParser#text_comparison.
    def enterText_comparison(self, ctx:text2sqlParser.Text_comparisonContext):
        pass

    # Exit a parse tree produced by text2sqlParser#text_comparison.
    def exitText_comparison(self, ctx:text2sqlParser.Text_comparisonContext):
        if ctx.like() is not None:
            print('%\'', end='')


    # Enter a parse tree produced by text2sqlParser#numeric_column.
    def enterNumeric_column(self, ctx:text2sqlParser.Numeric_columnContext):
        pass

    # Exit a parse tree produced by text2sqlParser#numeric_column.
    def exitNumeric_column(self, ctx:text2sqlParser.Numeric_columnContext):
        pass


    # Enter a parse tree produced by text2sqlParser#operator.
    def enterOperator(self, ctx:text2sqlParser.OperatorContext):
        pass

    # Exit a parse tree produced by text2sqlParser#operator.
    def exitOperator(self, ctx:text2sqlParser.OperatorContext):
        pass


    # Enter a parse tree produced by text2sqlParser#gt.
    def enterGt(self, ctx:text2sqlParser.GtContext):
        print('> ', end='')

    # Exit a parse tree produced by text2sqlParser#gt.
    def exitGt(self, ctx:text2sqlParser.GtContext):
        pass


    # Enter a parse tree produced by text2sqlParser#lt.
    def enterLt(self, ctx:text2sqlParser.LtContext):
        print('< ', end='')

    # Exit a parse tree produced by text2sqlParser#lt.
    def exitLt(self, ctx:text2sqlParser.LtContext):
        pass


    # Enter a parse tree produced by text2sqlParser#eq.
    def enterEq(self, ctx:text2sqlParser.EqContext):
        print('= ', end='')

    # Exit a parse tree produced by text2sqlParser#eq.
    def exitEq(self, ctx:text2sqlParser.EqContext):
        pass


    # Enter a parse tree produced by text2sqlParser#like.
    def enterLike(self, ctx:text2sqlParser.LikeContext):
        print('LIKE \'%', end='')

    # Exit a parse tree produced by text2sqlParser#like.
    def exitLike(self, ctx:text2sqlParser.LikeContext):
        pass


    # Enter a parse tree produced by text2sqlParser#ordering.
    def enterOrdering(self, ctx:text2sqlParser.OrderingContext):
        pass

    # Exit a parse tree produced by text2sqlParser#ordering.
    def exitOrdering(self, ctx:text2sqlParser.OrderingContext):
        if ctx.order().asc() is not None:
            print('ASC ', end='')
        elif ctx.order().desc() is not None:
            print('DESC ', end='')
        print('LIMIT ', end='')
        if limit := ctx.parentCtx.INT():
            print(limit, end='')
        else:
            print(1, end='')


    # Enter a parse tree produced by text2sqlParser#order.
    def enterOrder(self, ctx:text2sqlParser.OrderContext):
        print('ORDER BY ', end='')
        if ctx.getText() in ('nieuwste', 'jongste', 'oudste') and ctx.parentCtx.column() is None:
            print('age ', end='')

    # Exit a parse tree produced by text2sqlParser#order.
    def exitOrder(self, ctx:text2sqlParser.OrderContext):
        pass


    # Enter a parse tree produced by text2sqlParser#desc.
    def enterDesc(self, ctx:text2sqlParser.DescContext):
        pass

    # Exit a parse tree produced by text2sqlParser#desc.
    def exitDesc(self, ctx:text2sqlParser.DescContext):
        pass


    # Enter a parse tree produced by text2sqlParser#asc.
    def enterAsc(self, ctx:text2sqlParser.AscContext):
        pass

    # Exit a parse tree produced by text2sqlParser#asc.
    def exitAsc(self, ctx:text2sqlParser.AscContext):
        pass


    # Enter a parse tree produced by text2sqlParser#value.
    def enterValue(self, ctx:text2sqlParser.ValueContext):
        print(ctx.getText(), end=' ')

    # Exit a parse tree produced by text2sqlParser#value.
    def exitValue(self, ctx:text2sqlParser.ValueContext):
        print(' ', end='')


    # Enter a parse tree produced by text2sqlParser#bool.
    def enterBool(self, ctx:text2sqlParser.BoolContext):
        pass

    # Exit a parse tree produced by text2sqlParser#bool.
    def exitBool(self, ctx:text2sqlParser.BoolContext):
        pass


    # Enter a parse tree produced by text2sqlParser#true.
    def enterTrue(self, ctx:text2sqlParser.TrueContext):
        print('1 ', end='')

    # Exit a parse tree produced by text2sqlParser#true.
    def exitTrue(self, ctx:text2sqlParser.TrueContext):
        pass


    # Enter a parse tree produced by text2sqlParser#false.
    def enterFalse(self, ctx:text2sqlParser.FalseContext):
        print('0 ', end='')

    # Exit a parse tree produced by text2sqlParser#false.
    def exitFalse(self, ctx:text2sqlParser.FalseContext):
        pass


    # Enter a parse tree produced by text2sqlParser#severity_scale.
    def enterSeverity_scale(self, ctx:text2sqlParser.Severity_scaleContext):
        pass

    # Exit a parse tree produced by text2sqlParser#severity_scale.
    def exitSeverity_scale(self, ctx:text2sqlParser.Severity_scaleContext):
        pass



del text2sqlParser