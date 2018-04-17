# -*- coding: UTF-8 -*-


def tag(name, *content, cls=None, **attrs):
    """生成一个或者多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' %
                           (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join(
            '<%s%s>%s</%s>' %
            (name, attr_str, c, name) for c in content
        )
    else:
        return '<%s%s />' % (name, attr_str)


def main():
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', id=33, cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'cls': 'framed'
    }
    print(tag(**my_tag))

if __name__ == '__main__':
    main()
