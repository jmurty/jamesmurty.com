Title: Ruby on Rails: errors when launching threads from a controller
Date: 2008-03-19 22:29
Author: James
Tags: Coding
Slug: ruby_on_rails_background_threads

While writing a proof-of-concept Ruby on Rails application (Ruby 1.8.6,
Rails 2.0.2) I was stumped by an intermittent problem where long-lived
processes would fail with the error message:

    :::text
    <ArgumentError: A copy of TransactionController has been removed from the module tree but is still active!>

Admittedly, I do some potentially dodgy things in this application. I
initiate a transaction in a TransactionController but cannot tell in
advance how long it will be until the transaction is finished – it may
succeed immediately or it may take several seconds. To keep the web site
visitor from waiting, the controller returns a result web page
immediately and spawns a Thread to continue processing the transaction
in the background. This thread updates one or more model objects as the
transaction's status changes, and these model objects are derived from a
plugin class.

The thread worked well in most cases, but it would fail when the
transaction took longer than a few seconds. The error seemed to be
triggered when the code created a new model object.

The workaround I found for this issue was to enable class caching in my
development environment. This caching is enabled by default in the
production environment but not in development. To enable it, I edited
the `config.cache_classes` property in the
*config/environments/development.rb* configuration file like so:

    :::ruby
    config.cache_classes = true

This setting disables class reloading in the development environment,
which means that you must restart the server before code changes will be
applied. This is a pain when you are developing an application, so I
only set this option to true when it is necessary to test slow
transactions.

I assume this issue is caused by Rails unloading the plugin's model
classes when it does a sweep looking for changed code files. It is a
shame this occurs even when no code changes have been made. And despite
the fact the error message names the controller class, in my testing the
error was only ever triggered by code that operated on model objects. If
I removed references to the models, the thread would do its job no
matter how long the transaction took.

I am no Rails expert so there is a good chance I am doing something
drastically wrong. I did spend some time looking for a better way to
spawn background thread tasks from a controller action, but the
suggestions I found involved running separate processes on the server
machine and communicating with them via sockets or shared database
tables – an arrangement that isn't much less hacky than what I'm
currently doing.

If you know of a saner way of doing this, please let me know in the
comments.
