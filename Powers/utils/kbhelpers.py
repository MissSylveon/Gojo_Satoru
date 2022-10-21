from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb(rows=None):
    if rows is None:
        rows = []
    lines = []
    for row in rows:
        line = []
        for button in row:
            btn_text = button.split(".")[1].upper()
            button = btn(btn_text, button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})
