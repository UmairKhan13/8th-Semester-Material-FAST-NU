<html>
<?php
header('P3P: CP="CAO PSA OUR"');

if(!isset($_SESSION))
{
    session_start();
}
if(isset($_POST["login"])){
    $userName=$_POST['userName'];
    $password=$_POST['password'];

    if($userName==='1')
    {
        echo "<script>";
        echo "window.parent.document.location.href='../trims.php#home';";
        echo "</script>";
    }
    else
    {
        echo "<script>";
        echo "window.parent.document.location.href='../trims.php#u1';";
        echo "</script>";
    }
}

?>
<head>
    <style>
        .form-group {
            margin-bottom: 1rem;
        }
        .form-control {
            display: block;
            width: 100%;
            padding: .375rem .75rem;
            font-size: 1rem;
            line-height: 1.5;
            color: #495057;
            background-color: #fff;
            background-clip: padding-box;
            border: 1px solid #ced4da;
            border-radius: .25rem;
            transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
            margin: 10px 0px;
        }

        .btn-block {
            display: block;
            margin:auto;
            width: 50%;
        }
    </style>
    <link rel="stylesheet" href="../style.css">

</head>

<body>
<div class="form-group">
    <p>PLEASE LOGIN</p>
    <form method="post" action="">
        <input name="Project Name" type="text" id="projectName" placeholder="Enter Your Project Name..." class="form-control">
        <input type="text" name="Tool Name" id="toolName">
        <input type="text" name="from" id="from">
        <input type="date" name="Date Taken" id="dateTaken" onchange="daysRequirementChange()">
        <input type="number" name="For Date" id="forDate" onchange="daysRequirementChange()">
        <p type="text" id="dateGiven"></p>
        <!--        <input type="submit" value="Log in" name="login" class="btn-block">-->
    </form>


    <script>
        let date = new Date();
        document.getElementById('dateTaken').value = getDateString(date);


        document.getElementById("forDate").value = 1;
        daysRequirementChange();

        function daysRequirementChange()
        {
            let dateTaken  = document.getElementById("dateTaken").value;
            let dateOfReturn = new Date(dateTaken);
            if(checkTimeGreaterThanCurrent(dateOfReturn))
            {
                let daysRequired = document.getElementById("forDate").value;
                dateOfReturn.setDate( dateOfReturn.getDate() + parseInt(daysRequired));
                document.getElementById('dateGiven').innerHTML=getDateString(dateOfReturn);
            }
            else
            {
                alert("selected date should not be previous than current");
            }

        }

        function getDateString(date)
        {
            let dateString = date.getFullYear()+"-";

            if(date.getMonth()<9)
            {
                dateString = dateString + "0";
            }
            dateString = dateString + (date.getMonth() + 1) + "-";
            if(date.getDate()<10)
            {
                dateString = dateString + "0";
            }
            dateString = dateString + (date.getDate())
            return dateString;
        }

        function checkTimeGreaterThanCurrent(someDate)
        {
            const today = new Date()
            if(someDate.getDate() == today.getDate() &&
                someDate.getMonth() == today.getMonth() &&
                someDate.getFullYear() == today.getFullYear())
            {
                return true;
            }
            else
            {
                if(today > someDate)
                {
                    return false;
                }
                else
                {
                    return true;
                }
            }
        }



    </script>
</div>
</body>

</html>