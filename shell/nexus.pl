#!/usr/bin/env perl

use strict;
use warnings;

use JSON::XS;

my $json = JSON::XS->new->canonical;

&printResult(&dispatch(@ARGV));

sub printResult {
    my $result = shift;
    print "$result";
}

sub dispatch {
    if(scalar(@_) == 0){
        &usage();
    }

    my $cmd = shift;
    my $result = undef;

    my %cmds = ( writeLinesF => \&call_writeLinesF
, hasExtensionF => \&call_hasExtensionF
, printL => \&call_printL
, isGzipF => \&call_isGzipF );

    if($cmd eq '-h' || $cmd eq '-?' || $cmd eq '--help' || $cmd eq '?'){
        &usage();
    }

    if(exists($cmds{$cmd})){
        $result = $cmds{$cmd}(@_);
    } else {
        print STDERR "Command '$cmd' not found\n";
        &usage();
    }

    return $result;
}


sub usage{
    print STDERR "The following commands are exported:\n";
    print STDERR "  writeLinesF\n";
    print STDERR q{    param 1: List Str}, "\n";
    print STDERR q{    param 2: Str}, "\n";
    print STDERR q{    return: ()}, "\n";
    print STDERR "  hasExtensionF\n";
    print STDERR q{    param 1: Str}, "\n";
    print STDERR q{    param 2: Str}, "\n";
    print STDERR q{    return: Bool}, "\n";
    print STDERR "  printL\n";
    print STDERR q{    param 1: List Str}, "\n";
    print STDERR q{    return: ()}, "\n";
    print STDERR "  isGzipF\n";
    print STDERR q{    param 1: Str}, "\n";
    print STDERR q{    return: Bool}, "\n";
    exit 0;
}



sub call_writeLinesF{
    if(scalar(@_) != 2){
        print STDERR "Expected 2 arguments to 'writeLinesF', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 1 '$_[0]' '$_[1]'`;
}


sub call_hasExtensionF{
    if(scalar(@_) != 2){
        print STDERR "Expected 2 arguments to 'hasExtensionF', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 2 '$_[0]' '$_[1]'`;
}


sub call_printL{
    if(scalar(@_) != 1){
        print STDERR "Expected 1 arguments to 'printL', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 3 '$_[0]'`;
}


sub call_isGzipF{
    if(scalar(@_) != 1){
        print STDERR "Expected 1 arguments to 'isGzipF', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 4 '$_[0]'`;
}


