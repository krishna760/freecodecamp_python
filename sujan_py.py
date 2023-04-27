# # Array
# # colors=['orange', 'green', 'red', 'yellow', 'brown', 'black']
# # for i, color in enumerate(colors):
#     # print("The index of", color, "is", i)
#   #dictonary
# sounds = {
#     "cat": "mew",
#     "dog": ["woof", "bark"],
#     "penguin": "meep",
#     "fox": "screech",
#     "duck": "honk",
#     "sheep": "baaa",
# }
# # sounds["tiger"]="grr"
# # a=sounds["tiger"]
# # print(sounds)
# for i in sounds.values():
#   for i in sounds.keys():
#     for i in sounds.items():
#       for animal, sound in sounds.items():
#         if animal == "dog":
#             print(animal, "goes: ", sound[0], "and", sound[1])
#         else:
#             print(animal, "makes this noise: ", sound)
        #  print("The sound of", animal, "is", sound)

#FILE HANDLING
#without using with
      # file = open('file_path', 'w')
      #print(file.readlines())
      # try:
      #     file.write('hello world')
      # finally:
      #     file.close()

# #with using with
# with open("demo.txt") as f:
#   for line in f:
#     e=line.strip()
#     print(e * 2)#end for not printing new line

with open('demo.txt') as a:
  for s in a:
    line=s.strip()
    print(line)