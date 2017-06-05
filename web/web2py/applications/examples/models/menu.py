# -*- coding: utf-8 -*-

response.menu = [
    (T('主页'), request.controller == 'default' and request.function == 'index', URL('default', 'index')),
    (T('关于'), request.controller == 'default' and request.function == 'what', URL('default', 'what')),
    (T('下载'), request.controller == 'default' and request.function == 'download', URL('default', 'download')),
    (T('文档 & 资源'), request.controller == 'default' and request.function == 'documentation', URL('default', 'documentation')),
    # (T('Support'), request.controller == 'default' and request.function == 'support', URL('default', 'support')),
    # (T('Contributors'), request.controller == 'default' and request.function == 'who', URL('default', 'who'))
]

#########################################################################
## Changes the menu active item
#########################################################################


def toggle_menuclass(cssclass='pressed', menuid='headermenu'):
    """This function changes the menu class to put pressed appearance"""

    positions = dict(
        index='',
        what='-108px -115px',
        download='-211px -115px',
        who='-315px -115px',
        support='-418px -115px',
        documentation='-520px -115px'
    )

    if request.function in positions.keys():
            jscript = """
            <script>
             $(document).ready(function(){
                         $('.%(menuid)s a').removeClass('%(cssclass)s');
                         $('.%(function)s').toggleClass('%(cssclass)s').css('background-position','%(cssposition)s')

             });
            </script>
            """ % dict(cssclass=cssclass,
                       menuid=menuid,
                       function=request.function,
                       cssposition=positions[request.function]
                       )

            return XML(jscript)
    else:
        return ''
