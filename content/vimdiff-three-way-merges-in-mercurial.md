Title: Vimdiff for three-way merges in Mercurial
Date: 2011-05-06 19:53
Author: James
Tags: Coding, Tips
Slug: vimdiff-three-way-merges-in-mercurial

I've been using [vim][] as my sole code editor for a couple of years now
at work. I find that the more I use it and the more I learn (there will
always be more to learn about vim) the happier I am with this fantastic
tool.

After working through some hairy code merges recently I realised I
needed a better approach than relying on inline diffs, where merge
conflicts are represented in a single file like so:

    :::diff
    <<<<<<< incoming
    Someone else's code
    =======
    My code
    >>>>>>> outgoing

Inline diffs are great for resolving relatively simple conflicts but can
quickly become confusing if conflicts span many lines or there are
significant differences between files.

So I configured Mercurial to open `vimdiff` upon merge
conflicts, but the default three-paned vertical-split view wasn't quite
what I wanted. It didn't include the base version of the conflicted
file, and the default window layout made it hard to see exactly what was
going on.

A little research turned up [a blog post][] showing how to better
configure vimdiff when using git. We use Mercurial at work so I adapted
this hint to work with Mercurial's [MergeProgram][] configuration:

    :::ini
    # Three-way merge with vimdiff (shows result in bottom window)
    # Based on http://mercurial.selenic.com/wiki/MergingWithVim
    # and http://www.toofishes.net/blog/three-way-merging-git-using-vim/

    [ui]
    merge = vimdiff

    [merge-tools]
    vimdiff.executable = vim
    vimdiff.args = -d -c "wincmd J" "$output" "$local" "$other" "$base"

This will show the merged file in a large window at the bottom with the
three pre-merge files of interest -- local changes, incoming/other
changes, the base file -- in a three-pane vertical split at the top.
With this set-up and some practice using the [vimdiff][] commands,
complex conflicting merges are much easier to deal with.

If you use `vim` or want to, be sure to check out the excellent
[Vim Casts][] video podcasts to learn (or re-learn) how to get the most
out of it. Some [recent episodes][] discuss `vimdiff` in the
context of a git workflow but are still full of useful pointers for
those not using git.

  [vim]: http://en.wikipedia.org/wiki/Vim_(text_editor)
  [a blog post]: http://www.toofishes.net/blog/three-way-merging-git-using-vim/
  [MergeProgram]: http://mercurial.selenic.com/wiki/MergeProgram
  [vimdiff]: http://vimdoc.sourceforge.net/htmldoc/diff.html
  [Vim Casts]: http://vimcasts.org/
  [recent episodes]: http://vimcasts.org/episodes/fugitive-vim-resolving-merge-conflicts-with-vimdiff/
