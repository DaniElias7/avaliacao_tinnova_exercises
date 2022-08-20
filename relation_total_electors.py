class Elections:

    def valid_votes(__self__, total, valids):
        '''Valid votes percentage in relation to the total number of voters'''
        result = ''

        percentage = (valids * 100) / total
        percentage_list = list(str(percentage))

        if percentage_list[percentage_list.index('.') + 1] == '0':
            return str(int(percentage)) + '%'

        result = 'Valid votes in relation to the total number of voters\n>> '+ str(percentage) + '%'

        return result

    def white_votes(__self__, total, whites):
        '''White votes percentage in relation to the total number of voters'''
        result = ''

        percentage = (whites * 100) / total
        percentage_list = list(str(percentage))

        if percentage_list[percentage_list.index('.') + 1] == '0':
            return str(int(percentage)) + '%'

        result = 'White votes in relation to the total number of voters\n>> '+ str(percentage) + '%'

        return result

    def null_votes(__self__, total, nulls):
        '''Null votes percentage in relation to the total number of voters'''
        result = ''

        percentage = (nulls * 100) / total
        percentage_list = list(str(percentage))

        if percentage_list[percentage_list.index('.') + 1] == '0':
            return str(int(percentage)) + '%'

        result = 'Null votes in relation to the total number of voters\n>> '+ str(percentage) + '%'

        return result

