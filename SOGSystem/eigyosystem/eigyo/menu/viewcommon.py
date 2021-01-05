# index画面
def indexview():
    indexes = {'system_name': '営業管理システム',
               'title': '営業管理システム',
               'nav': {
                   'eigyosystem:index': '営業管理システム',
               },
               'button': {
                   'eigyosystem:yosan': '予　算　管　理',
                   'eigyosystem:uriage': '売　上　管　理',
                   # 'eigyosystem:yosan': '受　注　管　理（開発中）',
                   # 'eigyosystem:yosan': '出　荷　管　理（開発中）',
                   # 'eigyosystem:yosan': '入　金　管　理（開発中）',
                   # 'eigyosystem:yosan': '顧　客　管　理（開発中）',
                   # 'eigyosystem:yosan': '見　積　管　理（開発中）',
                   # 'eigyosystem:yosan': '案　件　管　理（開発中）'
                   }
               }
    return indexes
