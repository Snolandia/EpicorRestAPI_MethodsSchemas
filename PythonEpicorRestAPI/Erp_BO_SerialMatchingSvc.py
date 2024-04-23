import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialMatchingSvc
# Description: Add your summary for this object here
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AutoMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipPartNum">Part.PartNum</param><param name="ipRevNum">PartRev.RevisionNum</param><param name="ipCrtHdr">ipCrtHdr</param><param name="opRevMsg">revision</param><param name="ds">The Serial Matching data set </param>
   OperationID: AutoMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSerialNum
   Description: Purpose:
Parameters:  none
Notes:type="Epicor.Mfg.BO.SerialMatchingDataSet"
<param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipPartNum">SerialNo.PartNum</param><param name="ipRevNum">PartRev.RevisionNum</param><param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opRevMsg">revision</param><param name="opnoBOMMsg">bommessage</param><return name="ds">The Serial Matching data set </return>
   OperationID: ChangeSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFullyMatched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFullyMatched
   Description: Purpose:
Parameters:  none
Notes:type="Epicor.Mfg.BO.SerialMatchingDataSet"
<param name="ipFullyMatched">ttSerialMatchHdr.FullyMatched</param><param name="ds">The Serial Matching data set </param>
   OperationID: ChangeFullyMatched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFullyMatched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFullyMatched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableToMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableToMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipType"></param><param name="ds">The Serial Matching data set </param>
   OperationID: GetAvailableToMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableToMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableToMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialMatchAsmbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialMatchAsmbl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipParAsmblSeqNum">parent assembly AsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: GetNewSerialMatchAsmbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMatchAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMatchAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialMatchMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialMatchMtl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipAsmblSeqNum">ipAsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: GetNewSerialMatchMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMatchMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMatchMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAsmblSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAsmblSerialNo
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode"></param><param name="ipSerialNum">SerialNo.SerialNumber</param><param name="ipInt"></param><param name="ds">The Serial Matching data set </param>
   OperationID: OnChangeAsmblSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAsmblSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAsmblSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSMAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSMAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode"></param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipAsmSeqNum"></param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateONSaveAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateONSaveAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerilaNum">ipSerilaNum</param><param name="ipAsmblSeqNum">ipAsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateONSaveAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateONSaveAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateONSaveAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMtlSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMtlSerialNo
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">revision</param><param name="ipSerialNum">Serial Number</param><param name="ipMtlSeqNum">ipMtlSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: OnChangeMtlSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSMMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSMMtl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">Part.PartNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSMMaterial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSMMaterial
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">Part.PartNum</param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipMtlSeqNum">ipMtlSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part.PartNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFullyMatched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFullyMatched
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipAssmblSeq">JobAsmbl.AssemblySeq</param><param name="ds">The Serial Matching data set </param>
   OperationID: SetFullyMatched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFullyMatched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFullyMatched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opQuestion"></param><param name="ds">The Serial Matching data set </param>
   OperationID: ValidateAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="opQuestion"></param>
   OperationID: ValidateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTopSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTopSerialNumber
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opErrMsg"></param>
   OperationID: ValidateTopSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTopSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTopSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlantLLSerTrk(epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantLLSerTrk
   Description: Purpose:
Parameters:  none
Notes:
<return name="opLLSerTrk">PlantConfCtrl.LowLvlSerialTrk</return>
   OperationID: GetPlantLLSerTrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantLLSerTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetMatchToParentAsmblSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatchToParentAsmblSerialNo
   OperationID: GetMatchToParentAsmblSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchToParentAsmblSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchToParentAsmblSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AutoMatch_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipSerialNo
   ipPartNum
   ipRevNum
   ipCrtHdr
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevNum:str = obj["ipRevNum"]
      self.ipCrtHdr:bool = obj["ipCrtHdr"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class AutoMatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRevMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFullyMatched_input:
   """ Required : 
   ipFullyMatched
   ds
   """  
   def __init__(self, obj):
      self.ipFullyMatched:bool = obj["ipFullyMatched"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class ChangeFullyMatched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSerialNum_input:
   """ Required : 
   ipSerialNo
   ipPartNum
   ipRevNum
   ipJobNum
   ipAssemblySeq
   """  
   def __init__(self, obj):
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevNum:str = obj["ipRevNum"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      pass

class ChangeSerialNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialMatchingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opRevMsg:str = obj["parameters"]
      self.opnoBOMMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AvailToMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number assigned to the SerialNo  """  
      self.IssueToAssembly:int = obj["IssueToAssembly"]
      """  Job Assembly Seq the SerialNo should be defined as a child of  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  MtlSeq the serial number was issued to.  """  
      self.Matched:bool = obj["Matched"]
      """  Indicates whether the serial number has been matched to a parent in SerialMatch.  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates if the serial number has been selected to be matched  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Sequence counter for this SerialMatchAsmbl record; required to keep the record unique because when the BOM is exploded to create the rows for the dataset, multiple records may be generated with the same assembly number (assembly SN will be null for all unmatched assembly qty).  """  
      self.AsmblSeqNum:int = obj["AsmblSeqNum"]
      self.BOMAssemblySeq:int = obj["BOMAssemblySeq"]
      """  AssemblySeq number of this assemby for the BOM  """  
      self.IsSerialTracked:bool = obj["IsSerialTracked"]
      """  Indicates whether this assembly is serial tracked. Non tracked assemblies are included because they may have serial tracked requirements.  """  
      self.TopPartNum:str = obj["TopPartNum"]
      """  Top SN part number. Used to relate SerialMatchAsmbl to SerialMatchHdr  """  
      self.TopSerialNum:str = obj["TopSerialNum"]
      """  Top SN serial number. Used to relate SerialMatchAsmbl to SerialMatchHdr  """  
      self.ReqByAsmblSeqNum:int = obj["ReqByAsmblSeqNum"]
      """  This will be the SeqNum from the SeiralMatchAsmbl record of the SerialMatchAsmbl record this material is required by. In the case where SerialMatchAsmbl part is not serial tracked, this will not be the same assembly sequence counter as in the ParentAsmblSeqNum.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  AssemblySeq for the assembly parent serial number.  """  
      self.ParentPartDesc:str = obj["ParentPartDesc"]
      """  Parent part number description from Part.PartDescription.  """  
      self.ParentAsmblSeqNum:int = obj["ParentAsmblSeqNum"]
      """  This will be the AsmblSeqNum from the SeiralMatchAsmbl record of the serial tracked parent assembly this material serial numberl will be matched to. In the case where the subassembly this subassembly is required by is not serial tracked, this will not be the same assembly sequence counter as in the ReqByAsmblSeqNum field. This relates the SerialMatchAsmbl record to its parent serial number SerialMatchAsmbl  """  
      self.AsmblPartNum:str = obj["AsmblPartNum"]
      """  Part number for the assembly serial number  """  
      self.AsmblSerialNo:str = obj["AsmblSerialNo"]
      """  Assembly serial number  """  
      self.AsmblPartDesc:str = obj["AsmblPartDesc"]
      self.QtyPer:int = obj["QtyPer"]
      """  Qty of this assembly required per parent assembly  """  
      self.PullQty:int = obj["PullQty"]
      """  PullQty for this assembly  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  OverRunQty for this assembly  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  RequiredQty for this assembly  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates whether this record was manually added using the Add Subassembly option in the Serial Matching UI. Set to true when a new entry is added in the UI.  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  Indicates if this assembly serial number has  all child serial numbers (material and subassembly) matched  """  
      self.ReqByAssemblySeq:int = obj["ReqByAssemblySeq"]
      self.RecNum:int = obj["RecNum"]
      self.BOMSeq:int = obj["BOMSeq"]
      self.BOMLevel:int = obj["BOMLevel"]
      self.ParRowIDent:str = obj["ParRowIDent"]
      self.FromReassignSNAsm:bool = obj["FromReassignSNAsm"]
      self.AsmblAttributeSetID:int = obj["AsmblAttributeSetID"]
      self.AsmblAttributeSetIDDesc:str = obj["AsmblAttributeSetIDDesc"]
      self.AsmblAttributeSetIDShortDesc:str = obj["AsmblAttributeSetIDShortDesc"]
      self.AsmblRevisionNum:str = obj["AsmblRevisionNum"]
      self.ParentAttributeSetID:int = obj["ParentAttributeSetID"]
      self.ParentAttributeSetIDDesc:str = obj["ParentAttributeSetIDDesc"]
      self.ParentAttributeSetIDShortDesc:str = obj["ParentAttributeSetIDShortDesc"]
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number for the Serial Number if this serial was created for the top level assembly of a job.  """  
      self.TopPartNum:str = obj["TopPartNum"]
      """  Part number for the parent serial number, from SerialNo.PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  When Serial Matching is in Job mode this is from JobHead RevisionNum; when in Serial mode with no job it will be for the part revision being used for matching.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  In Job Mode this is from JobHead PartDescription; in Serial Mode this is from Part.PartDescription  """  
      self.TopSerialNum:str = obj["TopSerialNum"]
      """  Parent serial number  """  
      self.SNStatus:str = obj["SNStatus"]
      """  Serial Number status from SerialNo.SNStatus  """  
      self.Quantity:int = obj["Quantity"]
      """  In Job Mode: The quantity of the part on the job. This will be the same for all entries for the same part/job in this table so that it can be displayed correctly in the UI, although each record in this table only represents a qty of 1 of the part; in Serial Mode the qty will always be 1.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The SerialNo CreateDate for the parent serial  """  
      self.EnableNewChildPart:bool = obj["EnableNewChildPart"]
      """  Indicates whether the UI form should enable the New Child Part menu option.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq of the parent part if related to a job  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  Indicates if this assembly serial number has  all child serial numbers (material and subassembly) matched  """  
      self.SourceIsJob:bool = obj["SourceIsJob"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence counter required to keep the record unique because when the BOM is exploded to create the rows for the dataset, multiple records may be generated with the same part number number (part SN will be null for all unmatched material qty).  """  
      self.TopPartNum:str = obj["TopPartNum"]
      """  Top SN part number. Used to relate SerialMatchMtl to SerialMatchHdr  """  
      self.TopSerialNum:str = obj["TopSerialNum"]
      """  Top SN serial number. Used to relate SerialMatchMtl to SerialMatchHdr  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  AssemblySeq for the assembly parent serial number.  """  
      self.ParentPartDesc:str = obj["ParentPartDesc"]
      """  Parent part number description from Part.PartDescription.  """  
      self.ReqByAsmblSeqNum:int = obj["ReqByAsmblSeqNum"]
      """  This will be the AsmblSeqNum from the SeiralMatchAsmbl record of the SerialMatchAsmbl record this material is required by. In the case where SerialMatchAsmbl part is not serial tracked, this will not be the same assembly sequence as in the ParentAsmblSeqNum field.  """  
      self.ParentAsmblSeqNum:int = obj["ParentAsmblSeqNum"]
      """  This will be the SeqNum from the SeiralMatchAsmbl record of the serial tracked parent assembly this material serial numberl will be matched to. In the case where the subassembly this material is required by is not serial tracked, this will not be the same assembly sequence counter as in the AsmblSeqNum field. This relates the SerialMatchMtl record to its parent serial number SerialMatchAsmbl  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  Part number for the material serial number  """  
      self.MtlSerialNo:str = obj["MtlSerialNo"]
      """  Material  serial number  """  
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      """  Material part number description from Part.PartDescription  """  
      self.BOMMtlSeq:int = obj["BOMMtlSeq"]
      """  MtlSeq number of this material requirement for the BOM  """  
      self.BOMAssemblySeq:int = obj["BOMAssemblySeq"]
      """  AssemblySeq number of this material requirement for the BOM  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Qty of this assembly required per parent assembly  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates whether this record was manually added using the Add Material option in the Serial Matching UI. Set to true when a new entry is added in the UI.  """  
      self.ParRowIDent:str = obj["ParRowIDent"]
      self.BOMMtlSeqNum:int = obj["BOMMtlSeqNum"]
      """  Sequence counter for material serial numbers  """  
      self.FromReassignSNAsm:bool = obj["FromReassignSNAsm"]
      self.MtlAttributeSetID:int = obj["MtlAttributeSetID"]
      self.MtlAttributeSetIDDesc:str = obj["MtlAttributeSetIDDesc"]
      self.MtlAttributeSetIDShortDesc:str = obj["MtlAttributeSetIDShortDesc"]
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      self.ParentAttributeSetID:int = obj["ParentAttributeSetID"]
      self.ParentAttributeSetIDDesc:str = obj["ParentAttributeSetIDDesc"]
      self.ParentAttributeSetIDShortDesc:str = obj["ParentAttributeSetIDShortDesc"]
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchingTableset:
   def __init__(self, obj):
      self.SerialMatchHdr:list[Erp_Tablesets_SerialMatchHdrRow] = obj["SerialMatchHdr"]
      self.SerialMatchAsmbl:list[Erp_Tablesets_SerialMatchAsmblRow] = obj["SerialMatchAsmbl"]
      self.SerialMatchMtl:list[Erp_Tablesets_SerialMatchMtlRow] = obj["SerialMatchMtl"]
      self.AvailToMatch:list[Erp_Tablesets_AvailToMatchRow] = obj["AvailToMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailableToMatch_input:
   """ Required : 
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class GetAvailableToMatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMatchToParentAsmblSerialNo_input:
   """ Required : 
   ipAsmSeq
   """  
   def __init__(self, obj):
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      pass

class GetMatchToParentAsmblSerialNo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewSerialMatchAsmbl_input:
   """ Required : 
   ipParAsmblSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipParAsmblSeqNum:int = obj["ipParAsmblSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class GetNewSerialMatchAsmbl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSerialMatchMtl_input:
   """ Required : 
   ipAsmblSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipAsmblSeqNum:int = obj["ipAsmblSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class GetNewSerialMatchMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPlantLLSerTrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLLSerTrk:int = obj["parameters"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangeAsmblSerialNo_input:
   """ Required : 
   ipMode
   ipSerialNum
   ipInt
   ds
   """  
   def __init__(self, obj):
      self.ipMode:str = obj["ipMode"]
      self.ipSerialNum:str = obj["ipSerialNum"]
      self.ipInt:int = obj["ipInt"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class OnChangeAsmblSerialNo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMtlSerialNo_input:
   """ Required : 
   ipMode
   ipSerialNum
   ipMtlSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipMode:str = obj["ipMode"]
      self.ipSerialNum:str = obj["ipSerialNum"]
      self.ipMtlSeqNum:int = obj["ipMtlSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class OnChangeMtlSerialNo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetFullyMatched_input:
   """ Required : 
   ipAssmblSeq
   ds
   """  
   def __init__(self, obj):
      self.ipAssmblSeq:int = obj["ipAssmblSeq"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class SetFullyMatched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateONSaveAssembly_input:
   """ Required : 
   ipSerilaNum
   ipAsmblSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipSerilaNum:str = obj["ipSerilaNum"]
      self.ipAsmblSeqNum:int = obj["ipAsmblSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class UpdateONSaveAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateSMAssembly_input:
   """ Required : 
   ipMode
   ipSerialNo
   ipAsmSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipMode:str = obj["ipMode"]
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipAsmSeqNum:int = obj["ipAsmSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class UpdateSMAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateSMMaterial_input:
   """ Required : 
   ipMode
   ipSerialNo
   ipMtlSeqNum
   ds
   """  
   def __init__(self, obj):
      self.ipMode:str = obj["ipMode"]
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipMtlSeqNum:int = obj["ipMtlSeqNum"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class UpdateSMMaterial_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateSMMtl_input:
   """ Required : 
   ipMode
   ds
   """  
   def __init__(self, obj):
      self.ipMode:str = obj["ipMode"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class UpdateSMMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAssembly_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

class ValidateAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opQuestion:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SerialMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateJob_input:
   """ Required : 
   ipJobNum
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      pass

class ValidateJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateTopSerialNumber_input:
   """ Required : 
   ipSerialNo
   ipJobNum
   ipAssemblySeq
   """  
   def __init__(self, obj):
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      pass

class ValidateTopSerialNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opErrMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

