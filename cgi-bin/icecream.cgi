#!/usr/bin/env perl

use warnings;
use strict;
use diagnostics;
use CGI ':standard';
use CGI::Carp 'fatalsToBrowser';

my $form = new CGI;

print $form->header;

$form->start_html('Test');

my $street = $form->param('street');
my $phno = $form->param('phone');
my @icecream = $form->param('type');

my @arr = ("chocolate", "vanilla", "strawberry", "mocha chip", "coffee crunch");

my $subtotal = 0;
my $price = 1.25;
my $tax = 0.0925;

if ( length ( $street ) < 1 || length ( $phno ) < 1 ) {
    print "Please go back and fill out both 'Street' and 'Phone Number'";
    exit(0);
}

if ( scalar @icecream < 1 ) {
    print "Please select at least 1 flavor";
    exit(0);
}

my @orderarr;
foreach my $i (@icecream) {
    my $ismatch = 0;
    foreach my $x (@arr) {
        if (lc($i) eq $x) {
            $ismatch = 1;
        }
    }
    if ($ismatch == 0) {
        print "Spoof attempt failed";
        exit(0);
    }
    $subtotal += $price;
    my $order = $i . ":\t\t\$" . $price . "<br>";
    push @orderarr, $order
}

print "<font size = 4>";
print "<b>Please review the contact information that you entered:</b>";
print "</font>";
print "<br> Street Address: " . $street . "<br> Phone Number: " . $phno . "<br><br>";
print "<font size = 4><b>Please review your order:</b></font><br>";
print "<pre>";

foreach my $i (@orderarr) {
    print $i;
}

print "</pre><pre><font size = 4>";

$tax = $subtotal * $tax;
my $total = $tax + $subtotal;

$subtotal = sprintf("%.2f", $subtotal);
$tax = sprintf("%.2f", $tax);
$total = sprintf("%.2f", $total);

print "Subtotal:\t\t\$" . $subtotal . "<br>";
print "Tax:\t\t\t\$" . $tax . "<br>"; 
print "<b>Order Total:\t\t\$" . $total . "</b>";
print "<br>";
print "</font></pre>";
print "</body>";
print "</html>";
