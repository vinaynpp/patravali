with open('file.txt', "r") as txtfile:
    txt = txtfile.read()
    print(txt)


    def builder(main: str, replace: str, replacewith: str) -> str:
        tukda = main.partition(replace)
        output = tukda[0] + replacewith + tukda[2]
        print(output)
        return output

    builder(builder(txt, '<<function name>>', 'funtionname'), '<<function input>>', 'code')
