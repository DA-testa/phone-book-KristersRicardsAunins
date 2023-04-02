#python3
#221RDC033
class Query:
    def __init__(self, query):
        self.type = query [0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

class phone_book:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def process_queries(queries):
    result = []
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            found = False
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    found = True
                    break
            if not found:
                new_contact = phone_book(cur_query.number, cur_query.name)
                contacts.append(new_contact)

        elif cur_query.type == 'del':
            for contact in contacts:
                if contact.number == cur_query.number:
                    contacts.pop(contact)
                    break

        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
