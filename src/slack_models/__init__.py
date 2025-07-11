"""
# slack-models

Pydantic Models for working with the Slack API

"""

from importlib import metadata

from ._models import (
    EVENT_MAP,
    # Block Kit Models
    ActionsBlock,
    AppMentionEvent,
    Authorization,
    BaseBlock,
    BaseBlockElement,
    BaseSlackEvent,
    Block,
    BlockElement,
    ButtonElement,
    Channel,
    ChannelCreatedEvent,
    ChannelDeletedEvent,
    ChannelRenameEvent,
    ChannelsSelectElement,
    CheckboxesElement,
    ConfirmationDialog,
    ContextBlock,
    ConversationsSelectElement,
    DatePickerElement,
    DatetimePickerElement,
    DividerBlock,
    EmailInputElement,
    EnterpriseUser,
    ExternalSelectElement,
    File,
    FileBlock,
    FileContent,
    FileCreatedEvent,
    FileDeletedEvent,
    FileInputElement,
    HeaderBlock,
    ImageBlock,
    ImageElement,
    InputBlock,
    MessageEdited,
    MessageEvent,
    MessageItem,
    NumberInputElement,
    Option,
    OptionGroup,
    OverflowElement,
    PlainTextInputElement,
    RadioButtonsElement,
    Reaction,
    ReactionAddedEvent,
    ReactionRemovedEvent,
    RichTextBlock,
    RichTextElement,
    RichTextList,
    RichTextPreformatted,
    RichTextQuote,
    RichTextSection,
    SectionBlock,
    SlackAppRateLimited,
    SlackEvent,
    SlackEventCallback,
    SlackUrlVerification,
    SlackWebhookPayload,
    StaticSelectElement,
    TeamJoinEvent,
    TextObject,
    TimePickerElement,
    URLInputElement,
    User,
    UserProfile,
    UsersSelectElement,
    VideoBlock,
)
from ._utils import parse_event

try:
    version = metadata.version('slack-models')
except metadata.PackageNotFoundError:
    # Fallback when running from source without installation
    version = '0.0.0-dev'

__all__ = [
    'EVENT_MAP',
    'AppMentionEvent',
    'Authorization',
    'BaseSlackEvent',
    'Channel',
    'ChannelCreatedEvent',
    'ChannelDeletedEvent',
    'ChannelRenameEvent',
    'EnterpriseUser',
    'File',
    'FileContent',
    'FileCreatedEvent',
    'FileDeletedEvent',
    'MessageEdited',
    'MessageEvent',
    'MessageItem',
    'Reaction',
    'ReactionAddedEvent',
    'ReactionRemovedEvent',
    'SlackAppRateLimited',
    'SlackEvent',
    'SlackEventCallback',
    'SlackUrlVerification',
    'SlackWebhookPayload',
    'TeamJoinEvent',
    'User',
    'UserProfile',
    # Block Kit Models
    'ActionsBlock',
    'BaseBlock',
    'BaseBlockElement',
    'Block',
    'BlockElement',
    'ButtonElement',
    'ChannelsSelectElement',
    'CheckboxesElement',
    'ConfirmationDialog',
    'ContextBlock',
    'ConversationsSelectElement',
    'DatePickerElement',
    'DatetimePickerElement',
    'DividerBlock',
    'EmailInputElement',
    'ExternalSelectElement',
    'FileBlock',
    'FileInputElement',
    'HeaderBlock',
    'ImageBlock',
    'ImageElement',
    'InputBlock',
    'NumberInputElement',
    'Option',
    'OptionGroup',
    'OverflowElement',
    'PlainTextInputElement',
    'RadioButtonsElement',
    'RichTextBlock',
    'RichTextElement',
    'RichTextList',
    'RichTextPreformatted',
    'RichTextQuote',
    'RichTextSection',
    'SectionBlock',
    'StaticSelectElement',
    'TextObject',
    'TimePickerElement',
    'URLInputElement',
    'UsersSelectElement',
    'VideoBlock',
    'parse_event',
    'version',
]
