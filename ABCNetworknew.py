import markovify
import argparse
# Implementing command line gui for for Gentoo users
parser = argparse.ArgumentParser(description='ABC markovify transformer ')
parser.add_argument('-o', action='store', dest='Biden2020', type=str,
                    help="Path to the file", required=True)
parser.add_argument('-n', action='store', dest='TT', 
                    default='Salad life matters', type=str, 
                    help='Name your song')
parser.add_argument('-c', action='store', dest='FakeTucker',
                    default='Demencia_Hello.txt', type=str,
                    help='Path to the output file')
args = parser.parse_args()
# Opening the file
ABCtext = open(args.Biden2020, "r")
ThePower = args.TT + "\n"
# Build the model.
text_model = markovify.Text(ABCtext, state_size=1)
# Print ten randomly-generated sentences
for i in range(10):
    C = text_model.make_sentence(tries=100)
    ThePower = ThePower+C+" \n"
    print(C)
BLDNM = open(args.FakeTucker, "w")
BLDNM.write(ThePower)
BLDNM.close()
ABCtext.close()
#  ^\ no sence (of music should I have to make such crap)
# P.C. 44 of cource (true number for best vegans here)
