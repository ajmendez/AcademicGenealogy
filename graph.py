#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' graph.py -- Academic tree graph
2014: Mendez
Useful reference:
https://github.com/pygraphviz/pygraphviz/blob/master/examples/simple.py
http://stackoverflow.com/questions/7020741/drawing-rendering-multiway-tree-in-python
http://www.graphviz.org/doc/info/attrs.html
'''

import codecs
import pygraphviz as PG

PEOPLE = {
    'Alison Coil':['Alexander Mendez', 'Mojegan Azadi'],
    # 'Marc Davis':['Alison Coil', 'George Djorgovski', 'Kate Ebneter', 'Avery Meiksin', 'Karl Fischer', 'Frank Summers', 'David Schlegel', 'Matt Graig', 'Leonidas Moustakas', 'Jeff Newman', 'Michael Cooper'],
    'Marc Davis':['Alison Coil'],
    # 'David Todd Wilkinson':['Marc Davis', 'Lawrence Rudnick', 'Peter R. Saulson', 'Peter Timbie'],
    'David Todd Wilkinson':['Marc Davis', 'Peter Timbie'],
    'H. Richard Crane':['David Todd Wilkinson'],
    'Charlie Lauritsen':['H. Richard Crane', 'William A. Fowler'],
    'Robert A. Millikan':['Charlie Lauritsen'],
    'Michael I. Pupin':['Robert A. Millikan'],
    'Hermann Helmholtz':['Michael I. Pupin', 'Albert Abraham Michelson'],
    u'Johannes Peter Müller':['Hermann Helmholtz'],
    'Philipp Franz von Walther':[u'Johannes Peter Müller'],
    'Christian von Weigel':['Philipp Franz von Walther', 'Karl Rudolphi'],
    'Johann Christian Erxleben':['Christian von Weigel'],
    u'Abraham Gotthelf Kästner':['Johann Christian Erxleben'],
    'Christian August Hausen':[u'Abraham Gotthelf Kästner', 'Carl Friedrich Gauss'],
    'Johann Christoph Wichmannshausen':['Christian August Hausen'],
    'Otto Mencke':['Johann Christoph Wichmannshausen'],
    'Jakob Thomasius':['Otto Mencke'],
    'Friedrich Leibniz':['Jakob Thomasius'],
    
    'Peter Timbie':['Brian Keating'],
    'Brian Keating':['Darcy Barron', 'Dave Boegetter'],
    
    'Neal Katz':['Dusan Keres'],
    'James Gunn':['Neal Katz'],
    'Guido Munch':['James Gunn'],
    'Subrahmanyan Chandrasekhar':['Guido Munch'],
    'William A. Fowler':['Subrahmanyan Chandrasekhar','George Fuller'],
    
    'George Fuller':['Chad Kishimoto', 'Christel Sutterley', 'John Cherry', 'Evan Grohs'],
    

    
    'Kim Griest':['Agnieszka Cieplak','Jonathan Whitmore'],
    'Joel Primack':['Kim Griest', 'Risa Wechslser', 'James Bullock'],
    # 'Joel Primack':['Kim Griest',  'Rachel Somerville',  'Risa Wechslser',  'TJ Cox',  'James Bullock'],
    'Sidney Drell':['Joel Primack'],
    'Sidney M. Dancoff':['Sidney Drell'],
    'Robert Oppenheimer':['Sidney M. Dancoff'],
    'Max Born':['Robert Oppenheimer'],
    'Carl Runge':['Max Born'],
    'Karl Weierstrass':['Carl Runge'],
    'Christof Gudermann':['Karl Weierstrass'],
    'Carl Friedrich Gauss':['Christof Gudermann'],
    
    'James Larkin':['Shelley Wright'],
    'Tom Murphy':['Eric Michelsen', 'Nathan Johnson'],
    'Tom Soifer':['James Larkin', 'Tom Murphy'],
    'Jim Houck':['Tom Soifer'],
    'Raymond Bowers':['Jim Houck'],
    'Kurt Mendelssohn':['Raymond Bowers'],
    'Sir Francis Simon':['Kurt Mendelssohn'],
    'Walther Nernst':['Sir Francis Simon'],
    'Friedrich Kohlrausch':['Walther Nernst'],
    'Wilhelm Eduart Weber':['Friedrich Kohlrausch'],
    'Johann Salomo Christoph Schweigger':['Wilhelm Eduart Weber'],
    'Franz August Wolf':['Johann Salomo Christoph Schweigger'],
    
    'Michael Brown':['Adam Burgasser'],
    'J. Davy Kirkpatrick':['Adam Burgasser'],
    
    'Arthur Wolfe':['Marc Rafelski','J. Xavier Prochaska'],
    'Rainer Kurt Sachs':['Arthur Wolfe'],
    'Peter Gabriel Bergmann':['Rainer Kurt Sachs'],
    'Philipp Frank':['Peter Gabriel Bergmann'],
    'Ludwig Boltzmann':['Philipp Frank'],
    u'Jožef Stefan':['Ludwig Boltzmann'],
    'Andreas von Ettingshausen':[u'Jožef Stefan'],
    'Ignaz Lindner':['Andreas von Ettingshausen'],
    'Georg Jurij Bartolomej Veha von Vega':['Ignaz Lindner'],
    'Gabriel Gruber':['Georg Jurij Bartolomej Veha von Vega'],
    'Nikolaus Boda Poda von Neuhaus':['Gabriel Gruber'],
} 









def fmt(name):
    '''name formatter function'''
    # fname = name.decode("utf-8").encode("ascii","ignore")
    try:
        fname = u'{}'.format(name)
    except:
        print name
        raise
    if len(fname) > 20:
        fname = u'\n'.join(fname.split())
    return fname


def makegraph():
    '''Make the graph'''
    
    # G = PG.AGraph(PEOPLE, encoding='UTF-8', directed=True,
    #               splines='true', style='setlinewidth(2)')
    G = PG.AGraph(encoding='UTF-8', directed=True, forcelabel=True,
                  splines='true', style='setlinewidth(2)')
    G.node_attr['style'] = 'filled'
    G.node_attr['fillcolor'] = 'gray'
    for advisor,students in PEOPLE.iteritems():
        for student in students:
            advisor, student = map(fmt, (advisor,student))
            G.add_edge(advisor, student)
    
    
    G.get_edge('Alison Coil','Alexander Mendez').attr['label'] = '[2014]'
    G.get_edge('Brian Keating','Darcy Barron').attr['label'] = '[2015]'
    G.get_edge('George Fuller','Evan Grohs').attr['label'] = '[2015]'
    G.get_edge('Tom Murphy','Nathan Johnson').attr['label'] = '[2014]'
    
    # save the graph in dot format
    G.write('../tree.dot')

    # pygraphviz renders graphs in neato by default, 
    # so you need to specify dot as the layout engine
    G.layout(prog='dot')
    # G.layout()
    G.draw('../tree.png')
    
    return G




if __name__ == '__main__':
    makegraph()