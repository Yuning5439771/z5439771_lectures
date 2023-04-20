# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
# f_suburbs.pop('Randwick')
# f_suburbs.pop('Kensington')
# f_suburbs.update({
#     'Fairfield': 18081,
#     'Fairfield East': 5273,
#     'Fairfield Heights': 7517,
#     'Fairfield West': 11575,
#     'Fairlight': 5840,
#     'Fiddletown': 233,
#    'Five Dock': 9356,
#     'Flemington': None,
#     'Forest Glen': None,
#     'Forest Lodge': 4583,
#     'Forestville': 8329,
#     'Freemans Reach': 1973,
#     'Frenchs Forest': 13473,
#     'Freshwater': 8866
# }
# )
# print(f_suburbs)

# list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
# list_b = ['good', 'nice', 'friendly']
#
# sol =list_a[1:7]
# sol.remove('bad')
# sol.append('including')
# sol.insert(2, 'good')
# sol.extend(list_b)
# print(sol)
# f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
#
# nf_suburbs = []
#
# for key in f_suburbs:
#     if key[0] != 'F':
#         nf_suburbs.append(key)
#
# for suburb in nf_suburbs:
#     f_suburbs.remove(suburb)
#
# f_suburbs.update({
#         'Fairfield',
#         'Fairfield East',
#         'Fairfield Heights',
#         'Fairfield West',
#         'Fairlight',
#         'Fiddletown',
#         'Five Dock',
#         'Flemington',
#         'Forest Glen',
#         'Forest Lodge',
#         'Forestville',
#         'Freemans Reach',
#         'Frenchs Forest',
#         'Freshwater',
# }
# )
# current = 21 # at this point, the 9th element of the sequence
# last = 13 # at this point, the 8th element of the sequence
# current, last = current+last, current
# print(current, last)
# a = True
#
# if a:
#      a('There')
# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for i in l:
#     if i[:6] !='Forest':
#         print(i)
# f_suburbs = dict()
# f_suburbs["Fairfield"] = 18081
# f_suburbs["Fairfield East"] = 5273
# f_suburbs["Fairfield Heights"] = 7517
# f_suburbs["Fairfield West"] = 11575
# f_suburbs["Fairlight"] = 5840
# f_suburbs["Fiddletown"] = 233
# f_suburbs["Five Dock"] = 9356
# f_suburbs["Flemington"] = None
# f_suburbs["Forest Glen"] = None
# f_suburbs["Forest Lodge"] = 4583
# f_suburbs["Forestville"] = 8329
# f_suburbs["Freemans Reach"] = 1973
# f_suburbs["Frenchs Forest"] = 13473
# f_suburbs["Freshwater"] = 8866
#
# for town, populaion in f_suburbs.items():
#     if town[:6] !='Forest' and populaion is not None:
#         print(f"{town}: {populaion}")
# for i in range(1,101):
#     if i % 3 ==0 and i % 5 != 0:
#         print(f'{i}: Fizz')
#     elif i % 5 ==0 and i % 3 !=0:
#         print(f'{i}: Buzz')
#     elif i % 5 ==0 and i % 3 ==0:
#         print(f'{i}: FIZZ BUZZ')
#     else:
# #         print(i)
# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for i in range(len(l)):
#     print(f'{i}: {l[i]}')

# first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
# middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
# last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
#
# for l in last_names:
#     for f in first_names:
#         for m in middle_names:
#             if m is not None:
#                 print(f"{f} {m} {l}")
#             else:
#                 print(f'{f} {l}')
# s = "This is my test String"
# def process_string(s):
#     L = s.split()
#     for i, word in enumerate(L):
#         if i % 2 == 0:
#             L[i] = word.lower()
#         else:
#             L[i] = word.upper()
#     return L
#
# print(process_string(s))
#
# def fizz_buzz_sumz(i):
#     sum = 0
#     for x in range(1,i+1):
#         if x % 3 == 0 and x % 5 ==0:
#             continue
#         elif x % 3 == 0:
#             sum += 3*x
#         elif x % 5 == 0:
#             sum += 5*x
#         else:
#             sum += x
#     return sum

prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = sorted([k for k in prc_dic.keys()])
prc_dic['2020-01-15'] = prc_dic.pop('3030-01-15')
