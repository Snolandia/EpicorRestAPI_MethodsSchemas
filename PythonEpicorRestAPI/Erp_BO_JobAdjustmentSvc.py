import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobAdjustmentSvc
# Description: Job Adjustment Business Logic
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CalcUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcUnitCost
   Description: This method should be run when any of the following fields change on the job material
adjustment sheet to recalcuate the extended unit cost;
ttJATrans.MtlUnitCost
ttJATrans.BurUnitCost
ttJATrans.LbrUnitCost
ttJATrans.SubUnitCost
ttJATrans.MtlBurUnitCost
   OperationID: CalcUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborAssemSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborAssemSeq
   Description: This method needs to be called when the Assembly changes on the material sheet.
   OperationID: ChangeLaborAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborComplete
   Description: This method should be invoked when the complete flag changes .
   OperationID: ChangeLaborComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborEmployeeNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborEmployeeNum
   Description: This method changes the name of the employee when the employee number changes.
   OperationID: ChangeLaborEmployeeNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborEmployeeNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborEmployeeNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborJobNum
   Description: This method validates the job number and resets the assembly and operation .
This validation is also performed when the transaction is committed.
   OperationID: ChangeLaborJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborOprSeq
   Description: This method needs to be called when the operation on the Labor sheet changes.
It validates the sequences  and pulls in some defaults .
   OperationID: ChangeLaborOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborType
   Description: Run this method when the labor type changes. Valid labor types are 's' setup or 'p'
production. This method will also set the ' complete ' flag appropriately.
   OperationID: ChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlAssemSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlAssemSeq
   Description: This method needs to be called when the Assembly changes on the material sheet.
   OperationID: ChangeMtlAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlExtCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlExtCost
   Description: This method should be run when the extended cost changes on the adjust material sheet.
   OperationID: ChangeMtlExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlJobMtl
   Description: This method should be invoked when the material changes. This method will find
the associated JobMtl record and reset the defaults.
   OperationID: ChangeMtlJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlJobNum
   Description: This method should be invoked when the material changes. This method will find
the associated JobMtl record and reset the defaults.
   OperationID: ChangeMtlJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlTranQty
   Description: Run this method after the TranQty on the JobMaterial sheet is changed. This method
will recalculate totals for the new tran amount.
   OperationID: ChangeMtlTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubAssemSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubAssemSeq
   Description: This method needs to be called when the Assembly changes on the subcontract sheet.
It clears out the JobSeq.
   OperationID: ChangeSubAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubExtCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubExtCost
   Description: Run this method after the ExtCost is changed on the Subcontract sheet.
This method will recalculate the total for SubUnitCost.
   OperationID: ChangeSubExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubJobNum
   Description: This method validates the job number and resets the assembly and operation .
This validation is also performed when the transaction is committed.
   OperationID: ChangeSubJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubOper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubOper
   Description: This method should be invoked when the Job Operation (JobSeq) on the SubContract
sheet changes. This method will find  .
   OperationID: ChangeSubOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubTranQty
   Description: Run this method after the TranQty is changed on the Subcontract sheet. This method will recalculate totals
for the new Unit Cost.
   OperationID: ChangeSubTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubUnitCost
   Description: Run this method after the SubUnitCost is changed on the Subcontract sheet.
This method will recalculate the ExtCost.
   OperationID: ChangeSubUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitLaborAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitLaborAdj
   Description: This method will validate and commit the Labor record .
   OperationID: CommitLaborAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitLaborAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitLaborAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitMaterialAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitMaterialAdj
   Description: This method will validate and commit the Material adjustment record .
Before this is run, it is assumed that the ChangeMtlTranQty, ChangeMtlJobNum,
ChangeMtlJobMtl, ChangeMtlExtCost or CalcUnitCost were invoked on leave of a
the related field.
   OperationID: CommitMaterialAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitMaterialAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitMaterialAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitSubcontractAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitSubcontractAdj
   Description: This method should be run to commit the SubContract adjustment.
   OperationID: CommitSubcontractAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitSubcontractAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitSubcontractAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCommitMaterialAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCommitMaterialAdj
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitMaterialAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCommitMaterialAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitMaterialAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCommitSubcontractAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCommitSubcontractAdj
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitSubcontractAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCommitSubcontractAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitSubcontractAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartAdjustments
   Description: Use this method to start the Adjustment process .
   OperationID: StartAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartLaborAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartLaborAdjustment
   Description: Use this method to start the Labor Adjustment process.
   OperationID: StartLaborAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartLaborAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartLaborAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartMaterialAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartMaterialAdjustment
   Description: This method starts the material adjustment process by creating a temp-table record with defaults.
Return added record
   OperationID: StartMaterialAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartMaterialAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartMaterialAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReportPartQtyAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReportPartQtyAllowed
   Description: Returns TRUE if Part Quantity Reporting is allowed for a given operation.
Notes: In order to be allowed the following conditions must be meet.
1. Must be final assembly (AssemblySeq = 0)
2. Must be the final operation.
3. Job must have more that one end part defined or has one or more Parts with PartPerOp > 1
/* NOTE: THIS IS A PUBLIC FUNCTION. HOWEVER, I DID NOT USE THE STANDARD TRY_PUBLIC/CATCH_PUBLIC.
THIS IS BECAUSE I WANT IT TO BE  CALLABLE BY THE CLIENT AND THE SERVER. IF A PUBLIC CALLS A PUBLIC
THE EXCEPTION MESSAGES WOULD GET CLEARED TOO EARLY.
*/
   OperationID: ReportPartQtyAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReportPartQtyAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportPartQtyAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateChargeRateForTimeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateChargeRateForTimeType
   Description: Validates if there is no valid Charge Rate according to selected Time Type.
This validation can also be found on BO/LaborApproval.
   OperationID: ValidateChargeRateForTimeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateChargeRateForTimeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateChargeRateForTimeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultTimeTypCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultTimeTypCd
   Description: This method defaults dataset fields when the TimeTypCd field changes.
   OperationID: DefaultTimeTypCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultTimeTypCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTimeTypCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultRoleCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: DefaultRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildJobOperPrjRoleList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildJobOperPrjRoleList
   Description: This proc will return the where clause for the role code combo
Customers
   OperationID: BuildJobOperPrjRoleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildJobOperPrjRoleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobOperPrjRoleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes method.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildJobOperPrjRoleList_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   ipEmpID
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  JobNum  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  AssemblySeq  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  OprSeq  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  EmpID  """  
      pass

class BuildJobOperPrjRoleList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.whereClause:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalcUnitCost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class CalcUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborAssemSeq_input:
   """ Required : 
   laborAssmSeq
   ds
   """  
   def __init__(self, obj):
      self.laborAssmSeq:int = obj["laborAssmSeq"]
      """  LaborDtl.AssemblySeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborAssemSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborComplete_input:
   """ Required : 
   laborDtlComplete
   ds
   """  
   def __init__(self, obj):
      self.laborDtlComplete:bool = obj["laborDtlComplete"]
      """  LaborDtl.complete  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborEmployeeNum_input:
   """ Required : 
   laborDtlEmployeeNum
   ds
   """  
   def __init__(self, obj):
      self.laborDtlEmployeeNum:str = obj["laborDtlEmployeeNum"]
      """  LaborDtl.EmployeeNum  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborEmployeeNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborJobNum_input:
   """ Required : 
   laborDtlJobNum
   ds
   """  
   def __init__(self, obj):
      self.laborDtlJobNum:str = obj["laborDtlJobNum"]
      """  LaborDtl.JobNum  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborOprSeq_input:
   """ Required : 
   laborDtlOprSeq
   ds
   """  
   def __init__(self, obj):
      self.laborDtlOprSeq:int = obj["laborDtlOprSeq"]
      """  LaborDtl.OprSeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborType_input:
   """ Required : 
   ttJALaborDtlLaborType
   ds
   """  
   def __init__(self, obj):
      self.ttJALaborDtlLaborType:str = obj["ttJALaborDtlLaborType"]
      """  ttJALaborDtl.LaborType  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlAssemSeq_input:
   """ Required : 
   mtlAssmSeq
   ds
   """  
   def __init__(self, obj):
      self.mtlAssmSeq:int = obj["mtlAssmSeq"]
      """  PartTran.AssemblySeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeMtlAssemSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlExtCost_input:
   """ Required : 
   ttJATransExtCost
   ds
   """  
   def __init__(self, obj):
      self.ttJATransExtCost:int = obj["ttJATransExtCost"]
      """  PartTran.ExtCost  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeMtlExtCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlJobMtl_input:
   """ Required : 
   partTranJobSeq
   ds
   """  
   def __init__(self, obj):
      self.partTranJobSeq:int = obj["partTranJobSeq"]
      """  PartTran.JobSeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeMtlJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlJobNum_input:
   """ Required : 
   partTranJobNum
   ds
   """  
   def __init__(self, obj):
      self.partTranJobNum:str = obj["partTranJobNum"]
      """  parttran.JobNum  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeMtlJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlTranQty_input:
   """ Required : 
   ttJATransTranQty
   ds
   """  
   def __init__(self, obj):
      self.ttJATransTranQty:int = obj["ttJATransTranQty"]
      """  ttJATrans.TranQty  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeMtlTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubAssemSeq_input:
   """ Required : 
   ttJATransAssemblySeq
   ds
   """  
   def __init__(self, obj):
      self.ttJATransAssemblySeq:int = obj["ttJATransAssemblySeq"]
      """  PartTran.AssemblySeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubAssemSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubExtCost_input:
   """ Required : 
   ttJATransExtCost
   ds
   """  
   def __init__(self, obj):
      self.ttJATransExtCost:int = obj["ttJATransExtCost"]
      """  parttran.ExtCost  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubExtCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubJobNum_input:
   """ Required : 
   ttJATransJobNum
   ds
   """  
   def __init__(self, obj):
      self.ttJATransJobNum:str = obj["ttJATransJobNum"]
      """  PartTran.JobNum  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubOper_input:
   """ Required : 
   ttJATransJobSeq
   ds
   """  
   def __init__(self, obj):
      self.ttJATransJobSeq:int = obj["ttJATransJobSeq"]
      """  PartTran.JobSeq  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubOper_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubTranQty_input:
   """ Required : 
   ttJATransTranQty
   ds
   """  
   def __init__(self, obj):
      self.ttJATransTranQty:int = obj["ttJATransTranQty"]
      """  PartTran.TranQty  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubUnitCost_input:
   """ Required : 
   ttJATransSubUnitCost
   ds
   """  
   def __init__(self, obj):
      self.ttJATransSubUnitCost:int = obj["ttJATransSubUnitCost"]
      """  PartTran.SubUnitCost  """  
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ChangeSubUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CommitLaborAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class CommitLaborAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CommitMaterialAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class CommitMaterialAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CommitSubcontractAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class CommitSubcontractAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultRoleCd_input:
   """ Required : 
   ds
   ipRoleCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.ipRoleCd:str = obj["ipRoleCd"]
      """  Proposed RoleCd change  """  
      pass

class DefaultRoleCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultTimeTypCd_input:
   """ Required : 
   ds
   ipTimeTypCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.ipTimeTypCd:str = obj["ipTimeTypCd"]
      """  Proposed TimeTypCd change  """  
      pass

class DefaultTimeTypCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_JAAsmblyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.HasLabor:bool = obj["HasLabor"]
      self.HasMaterial:bool = obj["HasMaterial"]
      self.HasSubContract:bool = obj["HasSubContract"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JAJobsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.JobSeq:int = obj["JobSeq"]
      self.OperType:str = obj["OperType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JALaborDtlRow:
   def __init__(self, obj):
      self.ClockInDate:str = obj["ClockInDate"]
      self.LaborNote:str = obj["LaborNote"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.ActProdHours:int = obj["ActProdHours"]
      self.ActSetupHours:int = obj["ActSetupHours"]
      self.ActBurCost:int = obj["ActBurCost"]
      self.ActLabCost:int = obj["ActLabCost"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.EmployeeName:str = obj["EmployeeName"]
      self.LaborQty:int = obj["LaborQty"]
      self.LaborType:str = obj["LaborType"]
      self.LaborHrs:int = obj["LaborHrs"]
      self.LaborCost:int = obj["LaborCost"]
      self.BurdenHrs:int = obj["BurdenHrs"]
      self.BurdenCost:int = obj["BurdenCost"]
      self.Complete:bool = obj["Complete"]
      self.OpComplete:bool = obj["OpComplete"]
      self.company:str = obj["company"]
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      self.OpCode:str = obj["OpCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.JcDept:str = obj["JcDept"]
      self.JobNum:str = obj["JobNum"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.LaborRoleCd:str = obj["LaborRoleCd"]
      """  Project Role Code  """  
      self.LaborDisTimeTypCd:bool = obj["LaborDisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.LaborDisPrjRoleCd:bool = obj["LaborDisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.LaborTimeTypeCd:str = obj["LaborTimeTypeCd"]
      """  Time Type Code  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JALaborPartRow:
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartQty:int = obj["PartQty"]
      self.ReportedQty:int = obj["ReportedQty"]
      self.PartDescription:str = obj["PartDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JATransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.TotalCost:int = obj["TotalCost"]
      self.ActUnitMtlCost:int = obj["ActUnitMtlCost"]
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.ActUnitSubCost:int = obj["ActUnitSubCost"]
      self.ActUnitLbrCost:int = obj["ActUnitLbrCost"]
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.ActUnitMtlBurCost:int = obj["ActUnitMtlBurCost"]
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.ActUnitTotalCost:int = obj["ActUnitTotalCost"]
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.Reference:str = obj["Reference"]
      self.VenName:str = obj["VenName"]
      self.ActUnitBurCost:int = obj["ActUnitBurCost"]
      self.VendNum:int = obj["VendNum"]
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.BaseIssuedQty:int = obj["BaseIssuedQty"]
      self.BaseTranQty:int = obj["BaseTranQty"]
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.BaseUOM:str = obj["BaseUOM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates whether the PartNum is flagged as serial tracked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JATransSubAsmblyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TranDate:str = obj["TranDate"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.IssuedQty:int = obj["IssuedQty"]
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      self.ExtSubCost:int = obj["ExtSubCost"]
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      self.TotalCost:int = obj["TotalCost"]
      self.ActUnitMtlCost:int = obj["ActUnitMtlCost"]
      self.ActUnitSubCost:int = obj["ActUnitSubCost"]
      self.ActUnitLbrCost:int = obj["ActUnitLbrCost"]
      self.ActUnitMtlBurCost:int = obj["ActUnitMtlBurCost"]
      self.ActUnitTotalCost:int = obj["ActUnitTotalCost"]
      self.TranQty:int = obj["TranQty"]
      self.ExtCost:int = obj["ExtCost"]
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      self.SubUnitCost:int = obj["SubUnitCost"]
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      self.BurUnitCost:int = obj["BurUnitCost"]
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      self.Reference:str = obj["Reference"]
      self.VenName:str = obj["VenName"]
      self.SysDate:str = obj["SysDate"]
      self.SysTime:int = obj["SysTime"]
      self.TranNum:int = obj["TranNum"]
      self.JobSeq:int = obj["JobSeq"]
      self.UM:str = obj["UM"]
      self.ActUnitBurCost:int = obj["ActUnitBurCost"]
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      self.ExtBurCost:int = obj["ExtBurCost"]
      self.VendNum:int = obj["VendNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.TranType:str = obj["TranType"]
      self.JobNum:str = obj["JobNum"]
      self.OpComplete:bool = obj["OpComplete"]
      """  The flag to indicate if the Subcontract Operation is complete  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobAdjustmentTableset:
   def __init__(self, obj):
      self.JALaborDtl:list[Erp_Tablesets_JALaborDtlRow] = obj["JALaborDtl"]
      self.JALaborPart:list[Erp_Tablesets_JALaborPartRow] = obj["JALaborPart"]
      self.JAAsmbly:list[Erp_Tablesets_JAAsmblyRow] = obj["JAAsmbly"]
      self.JAJobs:list[Erp_Tablesets_JAJobsRow] = obj["JAJobs"]
      self.JATrans:list[Erp_Tablesets_JATransRow] = obj["JATrans"]
      self.JATransSubAsmbly:list[Erp_Tablesets_JATransSubAsmblyRow] = obj["JATransSubAsmbly"]
      self.Jobs:list[Erp_Tablesets_JobsRow] = obj["Jobs"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypesMat:str = obj["parameters"]
      self.listAvailTranDocTypesSub:str = obj["parameters"]
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

class PreCommitMaterialAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class PreCommitMaterialAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class PreCommitSubcontractAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class PreCommitSubcontractAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class ReportPartQtyAllowed_input:
   """ Required : 
   ip_JobNum
   ip_AssemblySeq
   ip_OprSeq
   """  
   def __init__(self, obj):
      self.ip_JobNum:str = obj["ip_JobNum"]
      """  Job number  """  
      self.ip_AssemblySeq:int = obj["ip_AssemblySeq"]
      """  Assembly Sequence number  """  
      self.ip_OprSeq:int = obj["ip_OprSeq"]
      """  Operation Sequence number  """  
      pass

class ReportPartQtyAllowed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if the ReportPartQtyAllowed  """  
      pass

class StartAdjustments_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class StartAdjustments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartLaborAdjustment_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      pass

class StartLaborAdjustment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JALaborDtlRow] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartMaterialAdjustment_input:
   """ Required : 
   ds
   inJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.inJobNum:str = obj["inJobNum"]
      """  Job Number  """  
      pass

class StartMaterialAdjustment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JATransRow] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateChargeRateForTimeType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      pass

class ValidateChargeRateForTimeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAdjustmentTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

