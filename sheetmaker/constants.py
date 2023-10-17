"""Html Constant file."""

EMPTY_SHEET = """<!DOCTYPE html>
<html class="" lang="en">
    <head>
        <title>{0}</title>
        <meta charset="utf8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.10/clipboard.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <script src="https://code.jquery.com/jquery-3.6.1.min.js" integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ=" crossorigin="anonymous"></script>
        <style>
            <!-- css -->
        </style>
    </head>
    <body>
        <script> new ClipboardJS('.btn_copy');</script>
        <div id="content">
            <div id="body_inner">
                <div class="main_title_block">
                    <!-- header -->
                </div>
                <table cellspacing="0" cellpadding="0" width="100%">
                    <tbody><tr>
                        <!-- columns -->
                    </tr></tbody>
                </table>
                <div class="block_footer">
                    <!-- footer -->
                </div>
            </div>
        </div>
    </body>
</html>
<script>
    var div_copy = $('*.copy'), k = 0;
    div_copy.each(
    function(){{
        k += 1;
        $(this).attr('id', 'copy'+k);
        $(this).append('<button class="btn_copy no-print" data-clipboard-target="#copy' + k + '"><i class="fa-regular fa-clipboard"></i></button>');
    }});
</script>"""


COLOR_STYLE = """
    body {{
        background: #dddfdd none repeat scroll 0 0;
        color: #46473b;
        font-family: "Lucida Grande","Lucida Sans Unicode",Arial,Helvetica,sans-serif;
        font-size: 80%;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        text-align: center;
    }}
    @media print {{
        body{{background: white none repeat scroll 0 0;}}
    }}
    #content {{
        background: white none repeat scroll 0 0;
        margin: 0 auto;
        padding: 0;
        position: relative;
        text-align: left;
        width: 980px;
    }}   
    #body_inner {{
        padding: 20px;
    }}
    .main_title_block {{
        display: inline-flex;
        margin-bottom: 30px;
    }}
    .main_logo{{
        background-color: #000000;
        border-top: 10px solid {1};
        padding: 10px 20px;
        //width: 50%;
    }}
    .main_title {{
        padding-left: 4%;
        min-width:40vw;
    }}
    .block {{
        background: {0} none repeat scroll 0 0;
        border-bottom: 3px solid {0};
        border-radius: 3px;
        margin-bottom: 12px;
        padding-bottom: 0;
    }}
    .block_title {{
        //color: #fee5d3;
        color: #ffffff;
        margin: 0;
        padding: 6px 8px;
        text-align: left;
    }}
    i {{
        vertical-align: sub
    }}
    .block_text{{
        padding: 5px 10px;
        background: {1} none repeat scroll 0 0;
    }}
    .rows_table {{
        background: white none repeat scroll 0 0;
        border-collapse: collapse;
        margin: 0;
        padding: 0;
        page-break-inside: avoid;
        width: 100%;
    }}
    .row_even td{{
        background: {1} none repeat scroll 0 0;
        padding: 5px 10px;
    }}
    .row_odd td {{
        padding: 5px 10px;
    }}
    .block_footer {{
        margin-top: 20px;
        border-top: solid 3px #ccc;
        display: inline-flex;
        width: 100%
    }}
    .block_footer_inner {{
        display: inline-flex;
        margin-bottom: 4%;
        margin-left:0px;
    }}
    .image_footer {{
        width: 64px;
        height: auto;
        margin-top: 10px;
    }}
    .text_footer{{
        margin-top: 16px;
        margin-left: 10px;
    }}
    svg.icon{{
        max-width:150px;
        height:auto;
        margin:15px;
    }}
    tr.row_even div.copy, tr.row_odd div.copy, div.block_text.copy{{
        display:flex;
        justify-content: space-between;
    }}
    .btn_copy{{
        margin-left:2px;
        margin-right:2px;
    }}
    .fa-clipboard{{
      color:gray;
    }}
    @media print
    {{
        .no-print, .no-print *
        {{
            display: none !important;
        }}
    }}"""


COLUMNS1 = """<td class="column_1" width="100%" valign="top"> <!-- column1 --> </td>"""
COLUMNS2 = """<td class="column_1" width="50%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="50%" valign="top"> <!-- column2 --> </td>"""
COLUMNS3 = """<td class="column_1" width="32%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column2 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column3 --> </td><td class="column_space" width="2%"></td>"""


HEADER = """
<svg class="icon" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="845.7243" height="704.03133" viewBox="0 0 845.7243 704.03133" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="f1503154-f50a-4680-8aa4-587be41cac87" data-name="Group 2"><path id="a9e5a31c-10e6-4175-9779-4994367672f7-96" data-name="Path 4" d="M880.72383,762.75434l-1.464,19.525-29.773-9.762,12.2-14.643Z" transform="translate(-177.13785 -97.98434)" fill="#feb8b8"/><path id="f499a4aa-6a35-40fc-8432-e4c7ab26d048-97" data-name="Path 5" d="M989.08286,756.40934l-1.467,19.035-16.595,2.441-9.762-9.274,11.226-18.06Z" transform="translate(-177.13785 -97.98434)" fill="#feb8b8"/><path id="fb70bf31-eafd-4d8a-8310-5130d8d104e1-98" data-name="Path 6" d="M1001.28487,513.33633s13.179,15.619-3.417,39.536-36.607,47.346-36.607,47.346l-37.1,70.286s-19.036,68.822-23.429,70.774-6.833-5.857-4.393,2.44.976,7.81-.976,8.3-7.321-.488-5.369,2.929,3.417,3.417-.488,3.417-5.369-2.44-5.369.976-3.417,11.226-3.417,11.226-23.917-6.833-24.893-9.762,6.345-4.393,4.881-7.321-1.952-2.929-1.952-7.321,2.929-5.369,2.929-5.369,2.44-.976,1.464-2.929-4.881-.976,0-3.417,24.895-77.121,24.895-77.121,0-37.1,6.345-49.3,1.464-99.084,16.6-100.06S1001.28487,513.33633,1001.28487,513.33633Z" transform="translate(-177.13785 -97.98434)" fill="#2f2e41"/><path id="a89455c2-275d-4b70-b13c-192fbe474176-99" data-name="Path 7" d="M996.40382,541.15733l-2.929,75.655s14.643,73.215,9.762,95.667-1.464,19.524-4.393,23.429-5.369,1.952-2.929,5.369,3.9,4.393,0,8.3-5.857,13.179-5.857,13.179l-24.893-2.44s6.345-11.226,3.9-13.667-8.786,1.464-3.9-3.9,7.81-2.929,4.881-5.369-7.321-1.464-3.417-5.369,8.3-3.9,4.393-5.369-8.3,0-6.345-2.929,4.393-6.345,4.393-6.345l-5.857-44.417s-6.833-14.643-4.881-20.988-8.3-58.572-8.3-58.572Z" transform="translate(-177.13785 -97.98434)" fill="#2f2e41"/><path id="a3024be5-ad86-493a-9bfb-258ab58160a1-100" data-name="Path 8" d="M985.66786,766.17034s4.881-4.881,6.345-1.952,12.2,29.286,5.857,31.238-15.619,3.9-20.5,2.44-15.131-8.3-27.333-8.3-22.452-5.369-22.452-7.321-1.952-13.667,7.321-13.667,26.357-10.738,26.357-10.738,3.9-7.81,5.857-7.321.488,16.107.488,16.107S978.83186,777.39635,985.66786,766.17034Z" transform="translate(-177.13785 -97.98434)" fill="#2f2e41"/><path id="a57c92ce-496a-44de-934b-3ddd78679762-101" data-name="Path 9" d="M877.30785,772.51535s4.393-10.738,8.786-8.3,1.464,32.7,1.464,32.7-3.9,6.345-15.131,4.881-41-4.881-47.834-3.417-25.381-6.833-20.5-18.06c0,0,2.44-6.345,14.155-5.857s33.191-13.667,33.191-13.667,3.417-9.762,4.393-8.786,1.952,18.06,1.952,18.06S870.47484,778.37235,877.30785,772.51535Z" transform="translate(-177.13785 -97.98434)" fill="#2f2e41"/><circle id="fa315d33-3eeb-4d45-ab88-aeb0e9694c5a" data-name="Ellipse 2" cx="764.11101" cy="196.19599" r="28.31" fill="#feb8b8"/><path id="fbae87ba-2986-46ef-9932-134b7e0cae24-102" data-name="Path 10" d="M963.21288,296.13233s15.131,30.262,20.5,33.191-36.607,20.989-36.607,20.989-6.833-29.774-15.131-36.119S963.21288,296.13233,963.21288,296.13233Z" transform="translate(-177.13785 -97.98434)" fill="#feb8b8"/><path id="fc15680c-e415-4000-ac02-b1f296562473-103" data-name="Path 11" d="M919.77283,543.59733l-1.952,18.548s-20.988-7.321-14.155-20.988Z" transform="translate(-177.13785 -97.98434)" fill="#feb8b8"/><path id="ae3770ab-4aa4-41b9-9f4d-4c69df699916-104" data-name="Path 12" d="M911.47784,515.77634c14.643,15.615,92.247,2.436,92.247,2.436l-.972-11.225,9.762-10.243-2.927-47.837s8.78-22.45,10.243-56.617a30.78024,30.78024,0,0,0-.378-6.278c-5.032-30.607-54.87-50.32-56.239-49.857-.689.227-8.025,4.05-15.681,8.072-8.789,4.617-17.994,9.5-17.994,9.5-11.716,4.4-9.762,74.687-13.67,81.031s0,28.3,0,28.3l-4.39,20.987S896.83087,500.16132,911.47784,515.77634Z" transform="translate(-177.13785 -97.98434)" fill="#f0f0f0"/><path id="b41fb511-fd5e-48e5-b733-0d9230f6b6d5-105" data-name="Path 13" d="M958.78288,360.82433s13.667,41,10.738,68.822-34.655,107.382-34.655,107.382l-10.733,5.857v13.666l-7.553-20.458,20.77-43.428S911.43285,342.76534,958.78288,360.82433Z" transform="translate(-177.13785 -97.98434)" opacity="0.1" style="isolation:isolate"/><path id="efbdbf49-3b58-4bc5-8391-5fbab31acdf7-106" data-name="Path 14" d="M945.96487,348.52235c14.161-7.808,35.639,12.7,58.09,34.657,8.063,7.883,12.726,7.09,15.4,2.832-5.032-30.607-54.87-50.32-56.239-49.857-.689.227-8.025,4.05-15.681,8.072Z" transform="translate(-177.13785 -97.98434)" opacity="0.1" style="isolation:isolate"/><path id="a2828270-d54b-4ede-bb2b-8639f55947f0-107" data-name="Path 15" d="M945.97183,344.74934l5.857-16.107s40.024-19.036,66.381,0l4.393,27.333s3.9,45.393-18.548,23.429S960.12485,336.93934,945.97183,344.74934Z" transform="translate(-177.13785 -97.98434)" fill="#f0f0f0"/><path id="f68da632-d878-40c3-a103-67cfc5c970db-108" data-name="Path 16" d="M957.35687,354.21633s13.667,41,10.738,68.822-34.655,107.382-34.655,107.382l-10.738,5.861v13.667l-22.452-6.345,4.881-16.107s-7.81-9.762-2.44-12.691,4.393-19.036,4.393-19.036S910.01086,336.15633,957.35687,354.21633Z" transform="translate(-177.13785 -97.98434)" fill="#f0f0f0"/><path id="f57115f6-7f5b-4177-880b-f5eff1305e5b-109" data-name="Path 17" d="M966.48688,306.03134c-.462-2.188-.4-4.542-1.448-6.517-1.573-2.961-5.188-4.2-8.529-4.492-4.265-.371-8.562.367-12.833.075s-8.833-1.92-10.959-5.635c-.848-1.482-1.266-3.227-2.391-4.512-2.341-2.674-6.608-2.26-9.972-1.114s-6.873,2.82-10.312,1.924c-2.892-8.091.669-17.424,6.828-23.415s14.465-9.215,22.715-11.618c10.881-3.17,23.126-5.043,33.13.282,14.507,7.721,19.626,28.158,18.288,43.39-.506,5.758-1.333,12.278-5.988,16.165C978.19385,316.26233,968.54687,315.77333,966.48688,306.03134Z" transform="translate(-177.13785 -97.98434)" fill="#2f2e41"/><rect id="e1abf0e4-070b-4c82-8a12-ebedd4e3db02" data-name="Rectangle 1" x="0.26201" y="0.347" width="611.461" height="391.60699" fill="#e6e6e6"/><rect id="ace8bea0-82e8-49b8-a50c-1e1cb532084f" data-name="Rectangle 2" x="19.746" y="49.464" width="576.492" height="319.32199" fill="#fff"/><rect id="b540f353-e277-4512-bc56-a133cea2858b" data-name="Rectangle 3" width="611.461" height="25.977" fill="#376bd8"/><circle id="b2b285b5-c1c3-4b12-9710-2898c7239781" data-name="Ellipse 3" cx="19.30501" cy="13.281" r="4.815" fill="#fff"/><circle id="a5a428bb-42a2-4f57-9e6c-9979c01a2490" data-name="Ellipse 4" cx="37.58001" cy="13.281" r="4.815" fill="#fff"/><circle id="a9929a25-14ce-4464-bac9-4165f1e3fae6" data-name="Ellipse 5" cx="55.85501" cy="13.281" r="4.815" fill="#fff"/><path id="b4a2d72b-abc3-4d2f-a2b8-a2aff6897b26-110" data-name="Path 37" d="M297.74287,192.20533l-38.133,37.657,38.133,37.656,8.58-8.58-28.835-28.839,29.076-29.076Z" transform="translate(-177.13785 -97.98434)" fill="#376bd8"/><path id="b5120d89-6cbe-4bfa-9a1b-cf9b07deff91-111" data-name="Path 38" d="M328.98787,192.20533l38.132,37.657-38.132,37.656-8.58-8.58,28.837-28.838-29.078-29.077Z" transform="translate(-177.13785 -97.98434)" fill="#376bd8"/><path id="a31271bd-8e2f-469b-8cee-8b6db3f92f99-112" data-name="Path 65" d="M452.33185,201.65533c-3.119,0-5.647,1.794-5.647,4.006s2.528,4.006,5.647,4.006h266.214c3.119,0,5.647-1.794,5.647-4.006s-2.528-4.006-5.647-4.006Z" transform="translate(-177.13785 -97.98434)" fill="#e6e6e6"/><path id="bf577952-0fd5-43e0-be6b-ea1966b51a93-113" data-name="Path 78" d="M715.89888,421.13433h-447.838c-4.578,0-8.288-2.643-8.293-5.9v-79.042c.005-3.257,3.715-5.9,8.293-5.9h447.838c4.578,0,8.288,2.643,8.293,5.9v79.041C724.18788,418.49035,720.47688,421.13034,715.89888,421.13433Zm-447.838-88.484c-2.747,0-4.973,1.586-4.976,3.54v79.041c0,1.954,2.229,3.538,4.976,3.54h447.838c2.747,0,4.973-1.586,4.976-3.54v-79.039c0-1.954-2.229-3.538-4.976-3.54Z" transform="translate(-177.13785 -97.98434)" fill="#e6e6e6"/><circle id="f7f4957b-eaa8-456b-bf02-bacf7de3ef80" data-name="Ellipse 13" cx="137.04001" cy="277.695" r="20.036" fill="#e6e6e6"/><path id="fb0f055d-da6e-47f2-bb6d-7ff26d7b746a-114" data-name="Path 79" d="M370.68788,359.65533a4.006,4.006,0,0,0-.01037,8.012H559.54884a4.006,4.006,0,0,0,0-8.012Z" transform="translate(-177.13785 -97.98434)" fill="#376bd8"/><path id="bfcde504-8c45-4d21-843b-87b1f7e22ce0-115" data-name="Path 80" d="M370.68788,383.69235a4.006,4.006,0,0,0-.01037,8.012h81.27636a4.006,4.006,0,0,0,.01038-8.012H370.68788Z" transform="translate(-177.13785 -97.98434)" fill="#376bd8"/><path id="a66699ea-75f1-4575-b6d5-52b0b1f8e30c-116" data-name="Path 81" d="M450.38788,225.65533a4.019,4.019,0,0,0,0,8.012h174.47a4.019,4.019,0,0,0,0-8.012Z" transform="translate(-177.13785 -97.98434)" fill="#e6e6e6"/><path id="bbc4ca7b-25d4-4c7e-b3d4-0411f69bd48f-117" data-name="Path 82" d="M451.53583,249.65533c-2.679,0-4.851,1.794-4.851,4.006s2.172,4.006,4.851,4.006h228.7c2.679,0,4.851-1.794,4.851-4.006s-2.172-4.006-4.851-4.006Z" transform="translate(-177.13785 -97.98434)" fill="#e6e6e6"/></g></svg>
<table class="main_title">
    <tbody>
        <tr>
            <td><h1 style="margin: 0px;">{0}</h1></td>
        </tr>
        <tr><td><a href="{3}" target="_blank">{1}, {2}</a></td></tr>
        <tr>
          <td>
            <b>💡 pour [coller] le presse-papier dans une console, faire un clic droit.</b>
          </td>
        </tr>
    </tbody>
</table>
"""


FOOTER = """
<div class="block_footer_inner">
    <table class="text_footer"><tbody>
            <tr><td>{0}</td></tr>
            <tr><td>Fiche créée avec <a href="http://github.com/cosme12/cheatsheet-maker" target="_blank">CheatSheet Maker</a></td></tr>
        </tbody></table>
</div>
"""


ROWS_BLOCK_EVEN = """<tr class="row_even">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>"""
ROWS_BLOCK_ODD = """<tr class="row_odd">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>"""
ROWS_BLOCK = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <table class="rows_table">
                        <tbody>
                            {1}
                        </tbody>
                    </table>
                </div>"""


TEXT_BLOCK = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <div class="block_text">{1}</div>
                </div>"""


