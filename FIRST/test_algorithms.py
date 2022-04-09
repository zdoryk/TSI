# import inquirer
#
# questions = [
#   inquirer.List('algorithm',
#                 message="What algorithm do you need",
#                 choices=['DE', 'PSO'],
#             ),
# ]
# answers = inquirer.prompt(questions)
#
# match answers.get('algorithm'):
#     case 'DE':
#         questions = [
#             inquirer.List('end',
#                           message="What algorithm do you need",
#                           choices=['DE', 'PSO'],
#                           ),
#         ]
#         answers = inquirer.prompt(questions)
#     case 'PSO':
#         print('PSO')
