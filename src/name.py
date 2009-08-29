from name.analysis import Analysis


if __name__ == "__main__":
    analysis = Analysis()
    
    analysis.analyse_file('../data/greek_m.txt')
    
    print 'Vowels: count=%d' % (analysis.vowels_n)
    print '  a=%d' % (analysis.vowels['a'])
    print '  e=%d' % (analysis.vowels['e'])
    print '  i=%d' % (analysis.vowels['i'])
    print '  o=%d' % (analysis.vowels['o'])
    print '  u=%d' % (analysis.vowels['u'])
    
    print '\nConsonants: count=%d' % (analysis.consonants_n)
    print '  b=%d' % (analysis.consonants['b'])
    print '  c=%d' % (analysis.consonants['c'])
    print '  d=%d' % (analysis.consonants['d'])
    print '  f=%d' % (analysis.consonants['f'])
    print '  g=%d' % (analysis.consonants['g'])
    print '  h=%d' % (analysis.consonants['h'])
    print '  j=%d' % (analysis.consonants['j'])
    print '  k=%d' % (analysis.consonants['k'])
    print '  l=%d' % (analysis.consonants['l'])
    print '  m=%d' % (analysis.consonants['m'])
    print '  n=%d' % (analysis.consonants['n'])
    print '  p=%d' % (analysis.consonants['p'])
    print '  q=%d' % (analysis.consonants['q'])
    print '  r=%d' % (analysis.consonants['r'])
    print '  s=%d' % (analysis.consonants['s'])
    print '  t=%d' % (analysis.consonants['t'])
    print '  v=%d' % (analysis.consonants['v'])
    print '  w=%d' % (analysis.consonants['w'])
    print '  x=%d' % (analysis.consonants['x'])
    print '  y=%d' % (analysis.consonants['y'])
    print '  z=%d' % (analysis.consonants['z'])
    
    print '\nStart: count=%d' % (analysis.start_n)
    for char, n in analysis.start.iteritems():
        print '  %s=%d' % (char, n)
