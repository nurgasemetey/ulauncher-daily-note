# Daily Note Ulauncher extension

With this extension, you can quickly take notes that are saved in journal format like `2022-02-20.md`

## Demo
![Alt text](images/demo.gif)

## Settings

`Directory`

Directory path where notes are stored. By default, notes are stored in `notes` folder in your home directory. Example: `/home/nurgasemetey/Desktop/notes`

`File name format`

Filename format of note. Example: `%Y-%m-%d`(means that YEAR-MONTH-DAY - 2022-02-20). Note: because under the hood it uses Python, it is different that you can be used to be. Please look at https://strftime.org/ and configure according to your needs. In the meantime, I will try to adapt ISO format to this extension.

`File extension`

File extension. File will be saved with this extension. Example: `.txt`, `.md`