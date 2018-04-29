import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    count = 0
    for xml_file in glob.glob(path + '/*.xml'):
        count += 1
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df, count


def main(path):
    image_path = os.path.join(os.getcwd(), ('../Microglia/' + path))
    xml_df, count = xml_to_csv(image_path)
    xml_df.to_csv('glia_'+path+'_labels.csv', index=None)
    print('Successfully converted {} xmls to csv.'.format(count))


main('train_annotations')
main('test_annotations')
