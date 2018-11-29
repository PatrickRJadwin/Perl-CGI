#!/usr/bin/env perl

use warnings;
use strict;
use CGI ':standard';


my $form = new CGI;

print $form->header;

$form->start_html('Test');

my $street = $form->param('street');
my $phno = $form->param('phone');
my @icecream = $form->param('type');
