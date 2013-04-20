Title: Textmate: Use Command-Escape as a Shortcut to the Gear Menu
Date: 2008-06-22 19:18
Author: James
Tags: Tips
Slug: textmate-command-escape-shortcut

[Textmate][] is a superb text/code editor for the Mac that makes
extensive use of keyboard shortcuts to make your life easier.

One of the most important shortcuts in Textmate is Control-Escape, which
opens a "Gear" menu with important context-sensitive functions. However,
if you turn on the Screen Sharing or Remote Management features of your
Mac, you will find that the Control-Escape key combination no longer
works. The remote-access applications hijack this shortcut.

To continue using the default Control-Escape shortcut with Textmate, you
have no choice but to turn off all of the remote-access applications.

If this is not an option, you will need to configure Texmate to
recognise a new shortcut for the gear menu. Here are the steps to
substitute Command-Escape for the Control-Escape shortcut:

1.  Prevent the Command-Escape shortcut from starting Front Row, by
    opening the *Keyboard and Mouse* preferences and disabling the first
    shortcut option: "Hide and show Front Row"
2.  Remap the Gear activation key by setting an application property for
    Textmate with the following command (all on one line):

        :::console
        defaults write com.macromates.textmate OakBundleItemsPopUpMenuKeyEquivalent "@\033"

Relaunch Textmate, and you should now be able to use the Command-Escape
shortcut to access the gear menu.

You can find more information about Textmate shortcut keys and the
Control-Escape issue at the following links:

-   <http://blog.macromates.com/2005/key-bindings-for-switchers/>
-   <http://manual.macromates.com/en/expert_preferences#oakbundleitemspopupmenukeyequivalent>

  [Textmate]: http://macromates.com/
