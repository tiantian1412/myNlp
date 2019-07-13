import re
pattern_set = {
    re.compile(u"(\?|？)$"),
    re.compile(u"几|多少|什么|吗"),
    re.compile(u"是.*还是"),
    re.compile(u"是不是|对不对|有没有|能不能|可不可以"),
    re.compile(u"怎么|如何|怎能|怎样|怎不|怎许|多怎"),
    re.compile(u"(可以|能).*[么吗]"),
    re.compile(u"哪里|哪些|哪个|哪儿|在哪|哪有|哪能|哪位"),
    re.compile(u"多久|多长时间"),
    re.compile(u"是啥|有啥|说啥|为啥|干啥|要啥"),
    re.compile(u""),


}