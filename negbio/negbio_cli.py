"""
Usage:
    negbio_cli [--verbose] <command> [<args>...]

Options:
    --verbose   Print more information about progress.

The most commonly used negbio commands are:
    text2bioc
    normalize
    section_split
    ssplit
    parse
    ptb2ud
    dner_mm
    dner_chexpert
    neg
    neg_chexpert
    cleanup
"""
from subprocess import call
import logging
import os
from negbio.cli_utils import parse_args

if __name__ == '__main__':
    args = parse_args(__doc__, version='negbio version 2', options_first=True)
    logging.debug('CWD: %s', os.getcwd())

    argv = [args['<command>']] + args['<args>']
    if args['<command>'] == 'text2bioc':
        exit(call(['python', 'negbio/negbio_text2bioc.py'] + argv))
    elif args['<command>'] == 'normalize':
        exit(call(['python', 'negbio/negbio_normalize.py'] + argv))
    elif args['<command>'] == 'section_split':
        exit(call(['python', 'negbio/negbio_section_split.py'] + argv))
    elif args['<command>'] == 'ssplit':
        exit(call(['python', 'negbio/negbio_ssplit.py'] + argv))
    elif args['<command>'] == 'parse':
        exit(call(['python', 'negbio/negbio_parse.py'] + argv))
    elif args['<command>'] == 'ptb2ud':
        exit(call(['python', 'negbio/negbio_ptb2ud.py'] + argv))
    elif args['<command>'] == 'dner_mm':
        exit(call(['python', 'negbio/negbio_dner_matamap.py'] + argv))
    elif args['<command>'] == 'dner_chexpert':
        exit(call(['python', 'negbio/negbio_dner_chexpert.py'] + argv))
    elif args['<command>'] == 'neg':
        exit(call(['python', 'negbio/negbio_neg.py'] + argv))
    elif args['<command>'] == 'neg_chexpert':
        exit(call(['python', 'negbio/negbio_neg_chexpert.py'] + argv))
    elif args['<command>'] == 'cleanup':
        exit(call(['python', 'negbio/negbio_clean.py'] + argv))
    elif args['<command>'] in ['help', None]:
        exit(call(['python', 'negbio/negbio_cli.py', '--help']))
    else:
        exit("%r is not a negbio.py command. See 'negbio help'." % args['<command>'])
