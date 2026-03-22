import json
import argparse
from tw_rouge import get_rouge


def main(args):
    refs, preds = {}, {}

    with open(args.reference,encoding="utf-8") as file:
        for line in file:
            line = json.loads(line)
            refs[line['id']] = line['title'].strip() + '\n'

    with open(args.submission,encoding="utf-8") as file:
        for line in file:
            line = json.loads(line)
            preds[line['id']] = line['title'].strip() + '\n'

    keys = refs.keys()
    missing_preds = [key for key in keys if key not in preds]
    extra_preds = [key for key in preds if key not in refs]

    if missing_preds:
        preview = ', '.join(missing_preds[:5])
        raise ValueError(
            f"Submission is missing {len(missing_preds)} reference ids. "
            f"First missing ids: {preview}"
        )

    if extra_preds:
        preview = ', '.join(extra_preds[:5])
        print(
            f"Warning: submission contains {len(extra_preds)} ids not present in the reference set. "
            f"They will be ignored. First extra ids: {preview}"
        )

    refs = [refs[key] for key in keys]
    preds = [preds[key] for key in keys]

    print(json.dumps(get_rouge(preds, refs), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reference')
    parser.add_argument('-s', '--submission')
    args = parser.parse_args()
    main(args)
