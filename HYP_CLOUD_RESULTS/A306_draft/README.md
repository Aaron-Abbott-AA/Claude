# A306 draft — how the LOCAL HYP session delivers it

The cloud session could not reach the mailbox, so this is a packet kit, not a delivered packet.

1. Poll PRIMARY/to_claude for files newer than 13:01:14Z. Hash each one on the device.
2. Write `receipt.md`, listing the files received with their hashes (delivery only, not review). Write `acks.txt` with lines of the form `<filename> <sha256>`.
3. If any new PRIMARY message changes what A306 should say, edit `src/message_template.md` first. Keep the `{{UTC}}` and `{{RECEIPT}}` placeholders.
4. Run `python3 build_A306.py --utc <YYYYMMDDTHHMMZ> --receipt receipt.md --acks acks.txt --out <new empty dir>`.
5. Copy the output into PRIMARY/to_codex in the order printed: data files, then the message, then the MANIFEST last. Verify the hashes on the device before placing the MANIFEST. Never overwrite peer files.
6. Record the packet name in PROGRESS.md.

All content in `src/` was independently audited and revision-checked: see the notes, audits and reviews folders and PROGRESS.md.
