__author__ = 'Kalyan'
notes = '''
For this exercise, you are going to do 2 things that you typically do in a job -

 - picking tools that do want you want and then figuring out how to install and use them (google search, product
   documentation, stack overflow etc.).
 - performance measurements of some behavior as you scale some parameter.


1. The tool you must install and use is pygal - a charting module for python.
2. Create a line chart for the file write performance of the program you have written in the previous assignment for
   various values of buffers you can pass to open function.
   buffer values are scaled across 0, 1, 1k, 2k, 4k, 8k and
   file size values are 1k, 10k, 100k, 1m, 10m, 20m

   x axis is file size, y axis is time and you need a line chart for each buffer size. have an appropriate legend.

This is a free form assignment, so you need to fill up the code below. It will include your code to generate the file of
given size and the code to generate the chart. It must generate a 'io-perf.svg' file in the module directory.
'''



#to use the file write new function that you have written
import project_02
import sys
import pygal
def create_file_numbers_new(filename, size, each_buff):
    value = 0
    length = 0 # number of bytes written so far
    with open(filename, "w", each_buff) as f:
        while length < size-3:
            s = str(value) + '\n'
            length += len(s) + 1 # add how many bytes are in this write()
            f.write(s)
            value += 1
            length += len(s) + 1 # add how many bytes are in this write()
            f.write(s)
            value += 1

def main(argv=sys.argv):
    file_size_list = [1024,10240,102400,1024*1024,10*1024*1024,20*1024*1024]
    buffer_vals = [0,1,1024,2048,4096,8192]
    time_lists = []
    for each_buff in buffer_vals:
        list_time =[]
        for each_size in file_size_list:
            list_time.append(create_file_numbers_new("temp",each_size,each_buff))
        time_lists.append(list_time)

    line_chart = pygal.Line(human_readable=True)
    line_chart.title = "File I/O performance results !"
    line_chart.x_labels = ['1K', '10K', '100M', '1M', '10M', '20M']
    line_chart.add('Buff: 0',time_lists[0])
    line_chart.add('Buff: 1',time_lists[1])
    line_chart.add('Buff: 1k',time_lists[2])
    line_chart.add('Buff: 2k',time_lists[3])
    line_chart.add('Buff: 4k',time_lists[4])
    line_chart.add('Buff: 8k',time_lists[5])
    line_chart.render_to_file('io-perf.svg')


if __name__ == "__main__":
    main()