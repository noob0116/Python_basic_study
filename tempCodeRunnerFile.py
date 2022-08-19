for list in range(1,51):
    list_file = open("{0}주차.txt".format(list), 'w', encoding = "utf8")
    print("- {0} 주차 주간보고\n-부서 :\n이름 :\n업무 요약 :".format(list), file = list_file)
list_file.close()