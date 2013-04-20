Title: Gmail bug? Conversation labels do not apply to new messages
Date: 2008-03-13 12:00
Author: James
Tags: Tips
Slug: gmail-labelling-search-bug

Gmail has a nasty bug (or quirk) that I have only just discovered. It
explains why I sometimes have trouble searching for specific emails in
my archive. To use Gmail effectively you will need to know about this
bug, and how to avoid it.

#### Background

In Gmail, messages are automatically grouped together into a
conversation based on the subject line of the emails. When you reply to
a message, or receive a new message with the same subject line, it is
added to the conversation.

You can apply labels to a conversation to help organise your archive,
and to make it easier to search. For example, I label any JetS3t-related
emails I receive with the "jets3t" label. Once I have done this, any
responses I send or replies I receive can be found by searching for
conversations with the "jets3t" label.

#### Label Granularity – Conversation or Message?

I had assumed that Gmail applies labels at the conversation level. The
UI presentation implies that this is the case, because the label names
are displayed at the top of the conversation and it is not possible to
apply labels to individual messages. However, it seems that this is not
the way Gmail works.

Instead of a label being applied to a whole conversation, it looks like
the label is only applied to the messages in a conversation **at the
time you add the label**. Any messages that are added to the
conversation later on will not inherit this label.

#### Misleading search results

I have found several examples where label-based searches that seem
straight-forward will not return the results you expect. Two
particularly nasty cases where your search results may be misleading are
when you apply a star to an individual message in a conversation, or if
there is an attachment later on in a conversation. Let's look at a real
example of the latter case.

I received a JetS3t-related email with a feature request. I applied the
"jets3t" label to this conversation and then replied. After a couple of
emails back-and-forth, I sent a message with a PDF file attachment to
the person who requested the feature.

Now, let's say I want to find all the JetS3t-related conversations where
I have sent or received an attachment. The obvious search to perform
is:

    :::text
    label:jets3t has:attachment

However, this does not include my email in the results. I know it should
be there, so what gives? I try listing all the messages that have the
"jets3t" label:

    :::text
    label:jets3t

This search returns a list of conversations that includes the one in
which I sent the attachment, along with hundreds of others. I can also
find this particular conversation by searching for all of the messages
in my archive that have attachments:  

    :::text
    has:attachment

So why doesn't the joint search (`label:jets3t has:attachment`) find
this conversation? Because although the message I sent is inside a
"jets3t" conversation, the message itself is not associated with this
label. The message is only loosely associated with the "jets3t" label
because it happens to belong to a conversation in which *other* messages
have this label.

To make this particular search perform properly, I forced Gmail to
associate every message in the conversation with the "jets3t" label by
re-applying the label to the conversation. After doing this, the joint
search finally returned my email in its results.

#### Beware

This Gmail quirk makes it difficult to use label-based searches with
confidence. Unless you perform the tedious work-around of manually
re-applying your labels every time a new message is added to a
conversation, you cannot be sure that searches against a label name and
another criteria will return all the results you would expect.

This bug will affect any message-specific search criteria. In addition
to the starred message and attachment cases I have mentioned, it will
also affect searches against specific recipients or senders, and
searches against particular dates. You should also be aware that the
date shown next to a conversation in a label view can be misleading, as
it shows the date of the last *labelled message* rather than the date of
the last message in the conversation.

I have found a [couple][] of [mentions][] of this issue, one going back
a long time, so I can only assume that this bizarre and opaque behaviour
is the way it is meant to be?

  [couple]: http://groups.google.com/group/Gmail-ABCs/browse_frm/thread/37f340984faa564/5530f1ce1144fa5e?lnk=gst&q=label+conversation+search#5530f1ce1144fa5e
  [mentions]: http://groups.google.com/group/Gmail-Problem-solving/browse_frm/thread/3af7b7582eae0c66/36ce0fbd7407aeee?lnk=gst&q=label+apply+search#36ce0fbd7407aeee
