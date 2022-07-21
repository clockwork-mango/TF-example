from perinuclearity import *

nucname = 'black nucleous.tif'
outsidename = 'black outside.tif'
redname = 'red.tif'


def process_folder(numlist, base_filename_list, target_folder, nucname, outsidename):
    compute_folder = True
    if compute_folder:
        for base_filename in base_filename_list[:]:
            print('Processing file {0}'.format(base_filename))
            target_file = target_folder + '/' + base_filename
            compute_perinuclearity_for_data(
                target_nucleus_file=target_file + nucname,
                target_periphery_file=target_file + outsidename,
                target_labels_file=target_file + redname,
                bkg_correction=0,
                do_show=False
            )

    # f3 = plt.figure(3, figsize=(3,5))
    for pos, base_filename in enumerate(base_filename_list[:]):
        print('Loading file {0}'.format(base_filename))
        perivalues_w = np.load(target_folder + '/' + base_filename + 'red.tifperivalues-w.npy')
        mask = np.logical_and(perivalues_w > 0, perivalues_w < 1)
        if pos == 0:
            data = np.copy(perivalues_w[mask])
        else:
            data = np.concatenate((data, perivalues_w[mask]))

    np.save(target_folder + '_overall_perivalues.npy', data)

####### WT DATASET
numlist = list(range(11))
numlist.remove(0)
base_filename_list=['WT_{0} '.format(n) for n in numlist]
target_folder = 'data/WT'
process_folder(numlist, base_filename_list, target_folder, nucname, outsidename)

####### NC DATASET
numlist = list(range(11))
numlist.remove(0)
base_filename_list=['NC_{0} '.format(n) for n in numlist]
target_folder = 'data/NC'
process_folder(numlist, base_filename_list, target_folder, nucname, outsidename)

####### GTP DATASET
numlist = list(range(11))
numlist.remove(0)
base_filename_list=['GTP_{0} '.format(n) for n in numlist]
target_folder = 'data/GTP'
process_folder(numlist, base_filename_list, target_folder, nucname, outsidename)

####### GDP DATASET
numlist = list(range(11))
numlist.remove(0)
base_filename_list=['GDP_{0} '.format(n) for n in numlist]
target_folder = 'data/GDP'
process_folder(numlist, base_filename_list, target_folder, nucname, outsidename)
