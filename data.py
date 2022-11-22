# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# c_list = ["1", "A", "C", "D"]
#
# x_list = list(zip(a, b, c_list))
#
# dist_list = []
#
# # for i in c_list:
# #     for x in x_list:
# #         data = {
# #             i: x
# #         }
# #         dist_list.append(data)
# #
# #
# # print(dist_list)
#
#
#
#
# #use the tuple() function to display a readable version of the result:
#
# print(x_list)

IDs = ['chest', 'hand', 'head']

EmpInfo = [{'xs': '45cm', 'M': '50cm'},
           {'xxl': '100cm', 'S': '60cm'},
           {'xl': '200cm', 'xm': '300cm'}]

D = dict(zip(IDs, EmpInfo))

print(D)
