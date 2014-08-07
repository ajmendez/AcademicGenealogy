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
    'Hermann Helmholtz':['Michael I. Pupin', 'Henry A Rowland','Albert Michelson'],
    u'Johannes Peter Müller':['Hermann Helmholtz'],
    'Philipp Franz von Walther':[u'Johannes Peter Müller'],
    # 'Christian von Weigel':['Philipp Franz von Walther', 'Karl Rudolphi'],
    'Christian von Weigel':['Philipp Franz von Walther'],
    'Johann Christian Erxleben':['Christian von Weigel'],
    u'Abraham Gotthelf Kästner':['Johann Christian Erxleben', 'Karl Christian von Langsdorf'],
    'Christian August Hausen':[u'Abraham Gotthelf Kästner', 'Carl Friedrich Gauss'],
    'Johann Christoph Wichmannshausen':['Christian August Hausen'],
    # 'Johann Andreas Planer':['Christian August Hausen'],
    # 'Rudolf Jakob Camerarius':['Johann Andreas Planer'],
    # 'Elias Rudolph Camerarius':['Rudolf Jakob Camerarius'],
    # 'Georg Balthasar Metzger':['Elias Rudolph Camerarius'],
    'Otto Mencke':['Johann Christoph Wichmannshausen'],
    'Jakob Thomasius':['Otto Mencke'],
    'Friedrich Leibniz':['Jakob Thomasius'],
    
    
    
    'Peter Timbie':['Brian Keating'],
    'Brian Keating':['Darcy Barron', 'Stephanie Moyerman', 'Nathan Miller',
                     'Evan Bierman'],
    
    
    
    
    'Neal Katz':['Dusan Keres'],
    'James Gunn':['Neal Katz','Claire Nicole Lackner','Charlie Conroy','Edmund Bertschinger'],
    'Guido Munch':['James Gunn'],
    'Subrahmanyan Chandrasekhar':['Guido Munch','Jeremiah Ostriker'],
    'Arthur Stanley Eddington':['Subrahmanyan Chandrasekhar'],
    # 'Ralph H. Fowler':['Subrahmanyan Chandrasekhar'],
    'Ralph H. Fowler':['Paul Adrien Maurice Dirac','Subrahmanyan Chandrasekhar'],
    # 'Archibald V. Hill':['Ralph H. Fowler'],
    # 'Walter Morley Fletcher':['Archibald V. Hill'],
    # 'John Newport Langley':['Walter Morley Fletcher'],
    # 'Micheal Foster':['John Newport Langley'],
    # 'William Sharpey':['Micheal Foster'],
    # 'Thomas Henry Huxley':['Micheal Foster'],
    
    # 'Uros Seljak':['Nikhil Padmanabhan','Rachel Mandelbaum'],
    # 'Edmund Bertschinger':['Uros Seljak'],
    # 'Jeremiah Ostriker':['Edmund Bertschinger','Michael Blanton','Edmund Bertschinger'],
    
    'George Fuller':['Chad Kishimoto', 'Christel Sutterley', 'John Cherry', 
                     'G. Wendell Misch', 'Evan Grohs'],
    'William A. Fowler':['George Fuller'],
    
    
    
    # 1972: Bowen University of Arizona http://www.linkedin.com/pub/richard-rothschild/41/1b5/aa4
    # http://ucsd.worldcat.org/title/pion-proton-elastic-scattering-at-180-from-60-to-160-gevc/oclc/27367351&referer=brief_results
    'Richard Rothschild':['Elizabeth Rivers','Eve Armstrong','Slawomir Suchy',
                          'Thomas Thompson'],
    # 1954 University of Chicago
    # THE IONIZATION ENERGY LOSS OF MESONS IN A SODIUM-IODIDE SCITION CRYSTAL
    'Theodore Bowen':['Richard Rothschild'],
    
    
    
    # 1982, University of London David R. Tytler
    'David Tytler':['Aaron Day',"John O'Meara",'David Kirkman','Scott Burles'],
    # ? Alexander Boksenberg, Electron collision processes in dissociated molecular gases , , (1961)
    'Alexander Boksenberg':['David Tytler'],
    
    
    
    
    'Frank Shu':['Wing Kit Lee'],
    'Chia-Chiao Lin':['Frank Shu'],
    'Theodore von Karman':['Chia-Chiao Lin'],
    'Ludwig Prandtl':['Theodore von Karman'],
    u'August Otto Föppl':['Ludwig Prandtl'],
    # 'Christian Otto Mohr':['August Otto Föppl'],
    'Felix Christian Klein':[u'August Otto Föppl', 'Arnold Sommerfeld'],
    u'Julius Plücker':['Felix Christian Klein'],
    'Christian Ludwig Gerling':[u'Julius Plücker'],
    
    
    
    
    # 'Rudolf Peierls':['Fred Hoyle'],
    # 'Richard Eden':['Rudolf Peierls'],
    # 'Werner Heisenberg':['Richard Eden'],
    # 'Arnold Sommerfeld':['Werner Heisenberg'],
    
    # 'Paul Adrien Maurice Dirac':['Fred Hoyle'],
    # 'Maurice Henry Lecorney Pryce':['Fred Hoyle'],
    # 'Wolfgang Ernst Pauli':['Maurice Henry Lecorney Pryce'],
    # 'Arnold Sommerfeld':['Wolfgang Ernst Pauli'],
    
    # 'John von Neumann':['Maurice Henry Lecorney Pryce'],
    # 'Lipot Fejer':['John von Neumann'],
    # 'Hermann Schwarz':['Lipot Fejer'],
    
    
    
    # The observation of directly produced electrons and positrons in hadron-hadron collisions Columbia University, Physics Dept., 1975
    'Hans P. Paar':['David Boettger'],
    'Leon M. Lederman':['Hans P. Paar'],
    'Eugene T. Booth':['Leon M. Lederman'],
    'Ellis Howard Dixon':['Eugene T. Booth'],
    'Charles Elwood Mendenhall':['Ellis Howard Dixon'],
    'Harry Fielding Reid':['Charles Elwood Mendenhall'],
    'Henry A Rowland':['Harry Fielding Reid'],
    # # above
    # u'Johannes Peter Müller':['Hermann von Helmholtz'],
    # 'Karl Mayer':[u'Johannes Peter Müller'],
    # 'Wilhelm Gottfried Ploucquet':['Karl Mayer'],
    # 'Ferdinand Christoph Oetinger':['Wilhelm Gottfried Ploucquet'],
    # 'Michael Alberti':['Ferdinand Christoph Oetinger'],
    # 'Georg Ernst Stahl':['Michael Alberti'],
    # 'Gilberto Bernardini':['Leon M. Lederman'],  ? 
     # Ph.D. from Columbia Universit
    # Leon Lederman
    
    
    # JR Wilson? 
    'Michael Norman':['Stephen Skory','David Collins'],
    # 1952 Berkeley Roland	H.	Good,	Jr http://physics.berkeley.edu/Annual_NEWSLETTER_PDFs/2007_Fall.pdf
    'James R. Wilson':['Michael Norman'],
    # penn state 
    # PhD, University of Michigan 1951 Advisor:
    # Roland Hamilton Good Jr., ON THE THEORY OF FORBIDDEN BETA-TRANSITIONS , , 86 (1951)
    'Roland Hamilton Good':['James R. Wilson'],
    'George Uhlenbeck':['Roland Hamilton Good'],
    'Paul Ehrenfest':['George Uhlenbeck','Samuel Abraham Goudsmit'],
    
    
    #Patrick Henry Diamond, THEORY OF PHASE SPACE DENSITY GRANULATION IN MAGNETOPLASMA , , 0 (1979) 
    # http://library.mit.edu/F/3HKTRNKXACAR3DXMICE6FXLPYGED86SQ9VB4PLMKK5N8NYBJ3S-22025?func=find-b&amp=&amp=&find_code=OCA&request=32787608
    'Patrick Diamond':['Lei Zhao','Novimir Pablant','Yusuke Kosuga',],
    # http://www.worldcat.org/title/theory-of-phase-space-density-granulation-in-magnetoplasma/oclc/7060963?referer=di&ht=edition
    'Thomas Dupree':['Patrick Diamond'],
    #Thomas Henderson Dupree, SOLUTIONS OF THE WAVE EQUATION IN A LATTICE OF SPHERICAL SCATTERERS , , 0 (1960)
    # http://library.mit.edu/F/3HKTRNKXACAR3DXMICE6FXLPYGED86SQ9VB4PLMKK5N8NYBJ3S-22025?func=find-b&amp=&amp=&find_code=OCA&request=32787608
    'Philip Morse':['Thomas Dupree'],
    'Karl Compton':['Philip Morse'],
    'Owen Richardson':['Karl Compton'],
    # 'Joseph Thomson':['Owen Richardson'],
    
    
    
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
    'Carl Friedrich Gauss':['Christof Gudermann','Christian Ludwig Gerling'],
    
    
    
    'James Larkin':['Shelley Wright'],
    'Tom Murphy':['Eric Michelsen', 'Nathan Johnson'],
    'Tom Soifer':['James Larkin', 'Tom Murphy'],
    'Jim Houck':['Tom Soifer'],
    'Raymond Bowers':['Jim Houck'],
    'Kurt Mendelssohn':['Raymond Bowers'],
    'Sir Francis Simon':['Kurt Mendelssohn'],
    'Walther Nernst':['Sir Francis Simon'],
    'Friedrich Kohlrausch':['Walther Nernst'],
    'Wilhelm Eduart Weber':['Friedrich Kohlrausch', 'Hermann Schwarz'],
    'Johann Salomo Christoph Schweigger':['Wilhelm Eduart Weber'],
    # 'Franz August Wolf':['Johann Salomo Christoph Schweigger'],
    'Karl Christian von Langsdorf':['Johann Salomo Christoph Schweigger'],
    
    
    
    'Adam Burgasser':['Daniella Bardalez-Gagliuffi'],
    'Michael Brown':['Adam Burgasser'],
    'Hyron Spinrad':['Michael Brown'],
    'Imke de Pater':['Michael Brown'],
    'Harry van der Laan':['Imke de Pater'],
    'Martin Ryle':['Harry van der Laan'],
    'John Ratcliffe':['Martin Ryle'],
    'Edward Appleton':['John Ratcliffe'],
    'Ernest Rutherford':['Edward Appleton'],
    'Joseph Thomson':['Edward Appleton','Owen Richardson'],
    
    'J. Davy Kirkpatrick':['Adam Burgasser'],
    #Donald Wans McCarthy Jr., AN INFRARED SPATIAL INTERFEROMETER: DESIGN AND DISCOVERIES , , 160 (1976)
    'Donald W. McCarthy Jr':['J. Davy Kirkpatrick'],
    # Rice University in 1959
    'Frank J. Low':['Donald W. McCarthy Jr'],
    #Harold E. Rorschach Jr., RESISTANCE MINIMA IN METALS AT LOW TEMPERATURES , , (1952)
    'Harold E. Rorschach':['Frank J. Low'],
    # ? William Vermillion Houston
    # ? Cole / Michelson / Millikan
    'William Vermillion Houston':['Harold E. Rorschach'],
    'Alfred D. Cole':['William Vermillion Houston'],
    
    
    
    
    'Arthur Wolfe':['Marc Rafelski','J. Xavier Prochaska'],
    'Rainer Kurt Sachs':['Arthur Wolfe'],
    'Peter Gabriel Bergmann':['Rainer Kurt Sachs'],
    'Philipp Frank':['Peter Gabriel Bergmann'],
    'Ludwig Boltzmann':['Philipp Frank', 'Paul Ehrenfest'],
    u'Jožef Stefan':['Ludwig Boltzmann'],
    'Andreas von Ettingshausen':[u'Jožef Stefan'],
    'Ignaz Lindner':['Andreas von Ettingshausen'],
    'Georg Jurij Bartolomej Veha von Vega':['Ignaz Lindner'],
    'Gabriel Gruber':['Georg Jurij Bartolomej Veha von Vega'],
    'Nikolaus Boda Poda von Neuhaus':['Gabriel Gruber'],
    
    
    'Alberto Bolatto':['Karin Sandstrom'],
    #http://academictree.org/physics/tree.php?pid=36896
    'James Jackson':['Alberto Bolatto'],
    'Alan Barrett':['James Jackson'],
    'Charles Townes':['Alan Barrett'],
    'William Smythe':['Charles Townes'],
    'Henry Gale':['William Smythe'],
    'Albert Michelson':['Henry Gale'],
    # 'Hermann Helmholtz':['Albert Abraham Michelson'],
    
    
    
    'Andrea Ghez':['Quinn Konopacky'],
    #93 Caltech
    'Gerald Neugebauer':['Andrea Ghez', 'David Hogg'], 
        # 1960 Caltech photoproduction of negative and positive pions from deuterium.
        # http://phdtree.org/scholar/neugebauer-gerry/
    'Robert Walker':['Gerald Neugebauer'],
    'Boyce Dawkins McDaniel':['Robert Walker'],
    'Robert Fox Bacher':['Boyce Dawkins McDaniel'],
    'Samuel Abraham Goudsmit':['Robert Fox Bacher'],
} 









def fmt(name):
    '''name formatter function -- it failed on some of the utf names,
    after specifying utf-8 as the encoding to pygraphviz all is good.'''
    # Drop utf encoded names
    # fname = name.decode("utf-8").encode("ascii","ignore")
    fname = u'{}'.format(name) # TODO: add dates / university
    if len(fname) > 20:
        fname = u'\n'.join(fname.split())
    return fname


def makegraph():
    '''Make the graph'''
    
    # this actually handles everything, but I wanted to add
    # some nice formatting and the sort.
    # G = PG.AGraph(PEOPLE, encoding='UTF-8', directed=True,
    #               splines='true', style='setlinewidth(2)')
    G = PG.AGraph(encoding='UTF-8', directed=True, forcelabel=True,
                  size="25.7,8.3!", resolution=400,
                  splines='true', style='setlinewidth(4)')
                  
    G.node_attr['style'] = 'filled'
    G.node_attr['fillcolor'] = 'gray'
    for advisor,students in PEOPLE.iteritems():
        for student in students:
            advisor, student = map(fmt, (advisor,student))
            G.add_edge(advisor, student)
    
    
    G.get_edge('Adam Burgasser','Daniella\nBardalez-Gagliuffi').attr['label'] = '[2015]'
    G.get_edge('Alison Coil','Mojegan Azadi').attr['label'] = '[2016]'
    G.get_edge('Brian Keating','Darcy Barron').attr['label'] = '[2015]'
    G.get_edge('George Fuller','Evan Grohs').attr['label'] = '[2015]'
    G.get_edge('Tom Murphy','Nathan Johnson').attr['label'] = '[2014]'
    
    # save the graph in dot format
    G.write('../tree.dot')

    # use the dot program to structure the graph roughly vertically
    G.layout(prog='dot')
    # G.graph_attr.update(dpi=400)
    # G.graph_attr.update(size="12,12")
    # G.graph_attr.update(font_size=14)
    G.draw('../tree.png')
    
    return G




if __name__ == '__main__':
    makegraph()