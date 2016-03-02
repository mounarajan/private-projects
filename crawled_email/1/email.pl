use CGI qw/:standard/;
use Mail::VRFY;
use Mail::Verify;
my $emailaddress = $ARGV[0];
#my $code = Mail::VRFY::CheckAddress($emailaddress);
#print $code;

#my $q = new CGI;
#[...]
#my $email = $q->param("mouuuuun.88@gmail.com");
#my $email_ck = Mail::Verify::CheckAddress( $email );

#print $email_ck;
my $code = Mail::VRFY::CheckAddress(addr => $emailaddress,method  => 'extended',timeout => 12,debug   => 0);
if ($code == 0){
    print "Email is valid";
    #print $code."\n";
}
elsif ($code == 1){
    print "Please Provide and email address";
    print $code."\n";
}
elsif ($code == 2){
    print "There is a syntactical error in the email address";
    print $code."\n";
}
elsif ($code == 3){
    print "Email is not valid";
    print "There are no MX or A DNS records for the host in question";
    print $code."\n";
}
elsif ($code == 4){
    print "Email is not valid";
    print "There are no SMTP servers accepting connections";
    print $code."\n";
}
elsif ($code == 5){
    if ($emailaddress =~ m/.*yahoo\..*/){
        print "Email is valid";
        print $code."\n";
    }
    else{
        print "Email is not valid";
        print "All SMTP servers are misbehaving";
        print $code."\n";
    }
}
elsif ($code == 6){
    print "Email is not valid";
    #print $code."\n";
}
elsif ($code == 7){
    print "Email is not valid";
    #print $code."\n";
}
#my $english = Mail::VRFY::English($code);

#print $english;
