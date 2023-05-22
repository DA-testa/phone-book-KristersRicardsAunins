#python3
#221RDC033

class Query:
    def __init__(self, query):
        self.tips = query[0]
        self.skaitlis = int(query[1])
        if self.tips == 'add':
            self.name = query[2]

            
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))

    
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.tips == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.skaitlis == cur_query.skaitlis:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.tips == 'del':
            for j in range(len(contacts)):
                if contacts[j].skaitlis == cur_query.skaitlis:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.skaitlis == cur_query.skaitlis:
                    response = contact.name
                    break
            result.append(response)
    return result

#221RDC033
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
