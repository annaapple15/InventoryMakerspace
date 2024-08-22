filaments = {
    'Black': {'color':'black', 
                  'material':'abs', 
                  'total rolls': 7, 
                  'unopened': 1, 
                  'full opened': 2, 
                  'useable but not full': 1, 
                  'unuseable or almost empty':4,
                  },

    'Silver': {'color':'silver', 
                   'material':'abs',
                   'total rolls': 5, 
                   'unopened':0, 
                   'full opened': 1,
                   'useable but not full': 2,
                   'unuseable or almost empty': 4,
                   },
    
    'White': {'color': 'white',
              'material': 'abs',
              'total rolls': 6,
              'unopened': 2,
              'full opened': 2,
              'useable but not full':0,
              'unuseable or almost empty': 2,
    },
    'Bronze': {'color': 'bronze',
               'material': 'abs',
               'total rolls': 3,
               'unopened': 0,
               'full opened':1,
               'useable but not full': 0,
               'unuseable or almost empty': 2,
               },

    'Fluorescent Orange': {'color': 'fluorescent orange',
                           'material':'abs',
                           'total rolls': 1,
                           'unopened':0,
                           'full opened': 0,
                           'useable but not full':0,
                           'unuseable or almost empty': 1,
                           },
    
    'Red': {'color': 'red',
            'material': 'abs',
            'total rolls': 3,
            'unopened': 2,
            'full opened':0,
            'useable but not full':1,
            'unuseable or almost empty':0,
            },
    
    'Translucent Black': {'color': 'translucent black',
                          'material': 'abs',
                          'total rolls':3,
                          'unopened':0,
                          'full opened':0,
                          'useable but not full':0,
                          'unuseable or almost empty':3,
                        },
    
    'UV Reactive': {'color': 'UV reactive',
                    'material':'abs',
                    'total rolls':3,
                    'unopened':1,
                    'full opened':1,
                    'useable but not full':0,
                    'unuseable or almost empty':1,
                    },
    
    'Natural': {'color': 'natural',
                'material':'abs',
                'total rolls':7,
                'unopened':1,
                'full opened':1,
                'useable but not full':3,
                'unuseable or almost empty':2,
                },

    'Translucent Blue': {'color': 'translucent blue',
                         'material': 'abs',
                         'total rolls':2,
                         'unopened':0,
                         'full opened':0,
                         'useable but not full':0,
                         'unuseable or almost empty':2
                        },

    'Glow Green': {'color': 'glow green',
                   'material':'abs',
                   'total rolls':7,
                   'unopened':2,
                   'full opened':3,
                   'useable but not full':2,
                   'unuseable or almost empty':0,
                   },

    'Translucent Red': {'cplor':'translucent red',
                        'material':'abs',
                        'total rolls':4,
                        'unopened':1,
                        'full opened':1,
                        'useable but not full':0,
                        'unuseable or almost empty':2,
                        },
    
    'Fluorescent Green': {'color':'fluorescent green',
                          'material':'abs',
                          'total rolls':2,
                          'unopened':0,
                          'full opened':0,
                          'useable but not full':0,
                          'unuseable or almost empty':2,
                          },

    'Color Change Blue': {'color':'color change blue',
                          'material':'abs',
                          'total rolls':2,
                          'unopened':0,
                          'full opened':0,
                          'useable but not full':2,
                          'unuseable or almost empty':0,
                          },

    'Fluorescent Blue': {'color':'fluorescent blue',
                         'material':'abs',
                         'total rolls':1,
                         'unopened':0,
                         'full opened':0,
                         'useable but not full':1,
                         'unuseable or almost empty':0,
                         },
    
    'Copper': {'color':'copper',
               'material':'abs',
               'total rolls':2,
               'unopened':0,
               'full opened':1,
               'useable but not full':0,
               'unuseable or almost empty':1,
               },
}

def report_inventory(color, material, total_rolls):
    report = {'color':color, 'material': material, 'total rolls': total_rolls}
    inventory_report = f"{color},{material}, total rolls: {total_rolls}."
    return inventory_report.title()


