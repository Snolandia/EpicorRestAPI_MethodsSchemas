import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SplitJobSvc
# Description: This business object with take an existing job, allow the user to modify jobprod
           records and then create a new job to split the existing job into.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SplitJobs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SplitJobs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SplitJobs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobProdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SplitJobs",headers=creds) as resp:
           return await resp.json()

async def post_SplitJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SplitJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobProdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobProdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SplitJobs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SplitJobs_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company, JobNum, PartNum, OrderNum, OrderLine, OrderRelNum, WarehouseCode, TargetJobNum, TargetAssemblySeq, TargetMtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SplitJob item
   Description: Calls GetByID to retrieve the SplitJob item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SplitJob
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TargetJobNum: Desc: TargetJobNum   Required: True   Allow empty value : True
      :param TargetAssemblySeq: Desc: TargetAssemblySeq   Required: True
      :param TargetMtlSeq: Desc: TargetMtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobProdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SplitJobs(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SplitJobs_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company, JobNum, PartNum, OrderNum, OrderLine, OrderRelNum, WarehouseCode, TargetJobNum, TargetAssemblySeq, TargetMtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SplitJob for the service
   Description: Calls UpdateExt to update SplitJob. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SplitJob
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TargetJobNum: Desc: TargetJobNum   Required: True   Allow empty value : True
      :param TargetAssemblySeq: Desc: TargetAssemblySeq   Required: True
      :param TargetMtlSeq: Desc: TargetMtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobProdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SplitJobs(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SplitJobs_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company, JobNum, PartNum, OrderNum, OrderLine, OrderRelNum, WarehouseCode, TargetJobNum, TargetAssemblySeq, TargetMtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SplitJob item
   Description: Call UpdateExt to delete SplitJob item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SplitJob
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TargetJobNum: Desc: TargetJobNum   Required: True   Allow empty value : True
      :param TargetAssemblySeq: Desc: TargetAssemblySeq   Required: True
      :param TargetMtlSeq: Desc: TargetMtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SplitJobs(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobProdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobProd, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJobProd=" + whereClauseJobProd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, partNum, orderNum, orderLine, orderRelNum, warehouseCode, targetJobNum, targetAssemblySeq, targetMtlSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderNum=" + orderNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderLine=" + orderLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderRelNum=" + orderRelNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "targetJobNum=" + targetJobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "targetAssemblySeq=" + targetAssemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "targetMtlSeq=" + targetMtlSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJob
   Description: This method checks to see if it is valid to split the specified job.
   OperationID: CheckJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJob(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJob
   Description: This methods generates the next available job number from the JCSyst table.
   OperationID: GetNewJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessSplitJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessSplitJob
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreProcessSplitJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessSplitJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessSplitJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessValidate
   Description: This method will perform pre-update validations
It validates whether the serial numbers selected for the Split are valid based on serail matching requirements.
It will send message to inform the user if there is active labor for the job.
   OperationID: PreProcessValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessSplitJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessSplitJob
   Description: This method runs the split job process.  This should be ran after updating and
validating the jobprods that have been split.  This will create a new job with associated
records but with new quantities specified in the split quantities.
   OperationID: ProcessSplitJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessSplitJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSplitJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJobProd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJobProd
   Description: This method validates the JobProd record.
   OperationID: ValidateJobProd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJobProd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobProd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transactionSelectJobMtlWithUpdLock
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobProd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobProd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobProd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobProd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobProd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitJobSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobProdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobProdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Erp_Tablesets_JobProdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number. Used in tying record back to its parent JobHead record.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.ProdQty:int = obj["ProdQty"]
      """   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  """  
      self.WIPQty:int = obj["WIPQty"]
      """   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipBy:str = obj["ShipBy"]
      """  The Demand Link Due Date - Ship By  """  
      self.DemandLinkStatus:str = obj["DemandLinkStatus"]
      """  The demand link status  """  
      self.DemandLinkSource:str = obj["DemandLinkSource"]
      """  The demand linke source  """  
      self.MakeToType:str = obj["MakeToType"]
      """  The Make to type (i.e. Stock, Job, Order)  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID  """  
      self.CustName:str = obj["CustName"]
      """  The customer name.  """  
      self.StkWIPQty:int = obj["StkWIPQty"]
      """  The stock WIP quantity  """  
      self.OrdWIPQty:int = obj["OrdWIPQty"]
      """  The order WIP quantity  """  
      self.JHPartNum:str = obj["JHPartNum"]
      """  The jobhead part number  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  The jobasmbl part number.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The jobmtl part number.  """  
      self.JHPartDesc:str = obj["JHPartDesc"]
      """  The jobhead part description  """  
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      """  The jobasmbl part description.  """  
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      """  The jobmtl part description.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Calculated field OurStockQty, will update OrderRel.OurStockQty  """  
      self.MakeToStockQty:int = obj["MakeToStockQty"]
      """  The make to stock quantity  """  
      self.MakeToJobQty:int = obj["MakeToJobQty"]
      """  The make to job quantity  """  
      self.PullFromStockWarehouseCode:str = obj["PullFromStockWarehouseCode"]
      """  Pull from Stock warehouse code (orderrel.warehousecode  """  
      self.PullFromStockWarehouseDesc:str = obj["PullFromStockWarehouseDesc"]
      """  The pull from stock warehouse description  """  
      self.SplitQty:int = obj["SplitQty"]
      """  The split quantity for the demand.  """  
      self.MaxAllowedQty:int = obj["MaxAllowedQty"]
      """  Calculated quantity that could come from allocatedqty or accumulation from parttran.  """  
      self.TotalSplitQuantity:int = obj["TotalSplitQuantity"]
      """  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  """  
      self.Valid:bool = obj["Valid"]
      """  This is a field used in Split Job to determine if record has been validated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobProdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number. Used in tying record back to its parent JobHead record.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.ProdQty:int = obj["ProdQty"]
      """   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  """  
      self.WIPQty:int = obj["WIPQty"]
      """   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.PlanID:str = obj["PlanID"]
      """  PlanID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WIPToMiscShipment:bool = obj["WIPToMiscShipment"]
      """  Job will be shipped through a Misc Shipment directly from WIP when job is closed.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Num linked from RMA Disposition.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line linked from RMA Disposition.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt linked from RMA Disposition.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition linked from RMA Disposition.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMRNum  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMRActionNum  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID  """  
      self.CustName:str = obj["CustName"]
      """  The customer name.  """  
      self.DemandLinkSource:str = obj["DemandLinkSource"]
      """  The demand linke source  """  
      self.DemandLinkStatus:str = obj["DemandLinkStatus"]
      """  The demand link status  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.JHPartDesc:str = obj["JHPartDesc"]
      """  The jobhead part description  """  
      self.JHPartNum:str = obj["JHPartNum"]
      """  The jobhead part number  """  
      self.MakeToJobQty:int = obj["MakeToJobQty"]
      """  The make to job quantity  """  
      self.MakeToStockQty:int = obj["MakeToStockQty"]
      """  The make to stock quantity  """  
      self.MakeToType:str = obj["MakeToType"]
      """  The Make to type (i.e. Stock, Job, Order)  """  
      self.MaxAllowedQty:int = obj["MaxAllowedQty"]
      """  Calculated quantity that could come from allocatedqty or accumulation from parttran.  """  
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      """  The jobmtl part description.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The jobmtl part number.  """  
      self.OrdWIPQty:int = obj["OrdWIPQty"]
      """  The order WIP quantity  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Calculated field OurStockQty, will update OrderRel.OurStockQty  """  
      self.PullFromStockWarehouseCode:str = obj["PullFromStockWarehouseCode"]
      """  Pull from Stock warehouse code (orderrel.warehousecode  """  
      self.PullFromStockWarehouseDesc:str = obj["PullFromStockWarehouseDesc"]
      """  The pull from stock warehouse description  """  
      self.ShipBy:str = obj["ShipBy"]
      """  The Demand Link Due Date - Ship By  """  
      self.SplitQty:int = obj["SplitQty"]
      """  The split quantity for the demand.  """  
      self.StkWIPQty:int = obj["StkWIPQty"]
      """  The stock WIP quantity  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TotalSplitQuantity:int = obj["TotalSplitQuantity"]
      """  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Valid:bool = obj["Valid"]
      """  This is a field used in Split Job to determine if record has been validated.  """  
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      """  The jobasmbl part description.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  The jobasmbl part number.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.CustInactive:bool = obj["CustInactive"]
      """  Indicates a customer referenced on the record is inactive.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if a ShipTo referenced on the record is inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
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

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckJob_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      pass

class CheckJob_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   jobNum
   partNum
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   targetJobNum
   targetAssemblySeq
   targetMtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.targetJobNum:str = obj["targetJobNum"]
      self.targetAssemblySeq:int = obj["targetAssemblySeq"]
      self.targetMtlSeq:int = obj["targetMtlSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobProdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number. Used in tying record back to its parent JobHead record.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.ProdQty:int = obj["ProdQty"]
      """   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  """  
      self.WIPQty:int = obj["WIPQty"]
      """   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipBy:str = obj["ShipBy"]
      """  The Demand Link Due Date - Ship By  """  
      self.DemandLinkStatus:str = obj["DemandLinkStatus"]
      """  The demand link status  """  
      self.DemandLinkSource:str = obj["DemandLinkSource"]
      """  The demand linke source  """  
      self.MakeToType:str = obj["MakeToType"]
      """  The Make to type (i.e. Stock, Job, Order)  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID  """  
      self.CustName:str = obj["CustName"]
      """  The customer name.  """  
      self.StkWIPQty:int = obj["StkWIPQty"]
      """  The stock WIP quantity  """  
      self.OrdWIPQty:int = obj["OrdWIPQty"]
      """  The order WIP quantity  """  
      self.JHPartNum:str = obj["JHPartNum"]
      """  The jobhead part number  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  The jobasmbl part number.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The jobmtl part number.  """  
      self.JHPartDesc:str = obj["JHPartDesc"]
      """  The jobhead part description  """  
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      """  The jobasmbl part description.  """  
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      """  The jobmtl part description.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Calculated field OurStockQty, will update OrderRel.OurStockQty  """  
      self.MakeToStockQty:int = obj["MakeToStockQty"]
      """  The make to stock quantity  """  
      self.MakeToJobQty:int = obj["MakeToJobQty"]
      """  The make to job quantity  """  
      self.PullFromStockWarehouseCode:str = obj["PullFromStockWarehouseCode"]
      """  Pull from Stock warehouse code (orderrel.warehousecode  """  
      self.PullFromStockWarehouseDesc:str = obj["PullFromStockWarehouseDesc"]
      """  The pull from stock warehouse description  """  
      self.SplitQty:int = obj["SplitQty"]
      """  The split quantity for the demand.  """  
      self.MaxAllowedQty:int = obj["MaxAllowedQty"]
      """  Calculated quantity that could come from allocatedqty or accumulation from parttran.  """  
      self.TotalSplitQuantity:int = obj["TotalSplitQuantity"]
      """  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  """  
      self.Valid:bool = obj["Valid"]
      """  This is a field used in Split Job to determine if record has been validated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobProdListTableset:
   def __init__(self, obj):
      self.JobProdList:list[Erp_Tablesets_JobProdListRow] = obj["JobProdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobProdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number. Used in tying record back to its parent JobHead record.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.ProdQty:int = obj["ProdQty"]
      """   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  """  
      self.WIPQty:int = obj["WIPQty"]
      """   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.PlanID:str = obj["PlanID"]
      """  PlanID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WIPToMiscShipment:bool = obj["WIPToMiscShipment"]
      """  Job will be shipped through a Misc Shipment directly from WIP when job is closed.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Num linked from RMA Disposition.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line linked from RMA Disposition.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt linked from RMA Disposition.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition linked from RMA Disposition.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMRNum  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMRActionNum  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID  """  
      self.CustName:str = obj["CustName"]
      """  The customer name.  """  
      self.DemandLinkSource:str = obj["DemandLinkSource"]
      """  The demand linke source  """  
      self.DemandLinkStatus:str = obj["DemandLinkStatus"]
      """  The demand link status  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.JHPartDesc:str = obj["JHPartDesc"]
      """  The jobhead part description  """  
      self.JHPartNum:str = obj["JHPartNum"]
      """  The jobhead part number  """  
      self.MakeToJobQty:int = obj["MakeToJobQty"]
      """  The make to job quantity  """  
      self.MakeToStockQty:int = obj["MakeToStockQty"]
      """  The make to stock quantity  """  
      self.MakeToType:str = obj["MakeToType"]
      """  The Make to type (i.e. Stock, Job, Order)  """  
      self.MaxAllowedQty:int = obj["MaxAllowedQty"]
      """  Calculated quantity that could come from allocatedqty or accumulation from parttran.  """  
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      """  The jobmtl part description.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The jobmtl part number.  """  
      self.OrdWIPQty:int = obj["OrdWIPQty"]
      """  The order WIP quantity  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Calculated field OurStockQty, will update OrderRel.OurStockQty  """  
      self.PullFromStockWarehouseCode:str = obj["PullFromStockWarehouseCode"]
      """  Pull from Stock warehouse code (orderrel.warehousecode  """  
      self.PullFromStockWarehouseDesc:str = obj["PullFromStockWarehouseDesc"]
      """  The pull from stock warehouse description  """  
      self.ShipBy:str = obj["ShipBy"]
      """  The Demand Link Due Date - Ship By  """  
      self.SplitQty:int = obj["SplitQty"]
      """  The split quantity for the demand.  """  
      self.StkWIPQty:int = obj["StkWIPQty"]
      """  The stock WIP quantity  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TotalSplitQuantity:int = obj["TotalSplitQuantity"]
      """  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Valid:bool = obj["Valid"]
      """  This is a field used in Split Job to determine if record has been validated.  """  
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      """  The jobasmbl part description.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  The jobasmbl part number.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.CustInactive:bool = obj["CustInactive"]
      """  Indicates a customer referenced on the record is inactive.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if a ShipTo referenced on the record is inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
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

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SplitJobTableset:
   def __init__(self, obj):
      self.JobProd:list[Erp_Tablesets_JobProdRow] = obj["JobProd"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSplitJobTableset:
   def __init__(self, obj):
      self.JobProd:list[Erp_Tablesets_JobProdRow] = obj["JobProd"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   partNum
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   targetJobNum
   targetAssemblySeq
   targetMtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.targetJobNum:str = obj["targetJobNum"]
      self.targetAssemblySeq:int = obj["targetAssemblySeq"]
      self.targetMtlSeq:int = obj["targetMtlSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SplitJobTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SplitJobTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SplitJobTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobProdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobProd_input:
   """ Required : 
   ds
   jobNum
   partNum
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   targetJobNum
   targetAssemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.targetJobNum:str = obj["targetJobNum"]
      self.targetAssemblySeq:int = obj["targetAssemblySeq"]
      pass

class GetNewJobProd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNextJobNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobProd
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobProd:str = obj["whereClauseJobProd"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SplitJobTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   ipJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Num before split  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class PreProcessSplitJob_input:
   """ Required : 
   ds
   ipDueDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.ipDueDate:str = obj["ipDueDate"]
      """  The due date  """  
      pass

class PreProcessSplitJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      self.SerialNumberQtyAlert:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreProcessValidate_input:
   """ Required : 
   ipJobNum
   splitQty
   ipDoLbrCheck
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  The input jobnum to split.  """  
      self.splitQty:str = obj["splitQty"]
      """  The qty to be split  """  
      self.ipDoLbrCheck:bool = obj["ipDoLbrCheck"]
      """  Flag to indicate whether to check for active labor  """  
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

class PreProcessValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.opLbrMessage:str = obj["parameters"]
      self.opSerialMatchMsg:str = obj["parameters"]
      self.opSerialNumber:str = obj["parameters"]
      self.opSerialMatchErr:bool = obj["opSerialMatchErr"]
      self.opLLTrkWarning:str = obj["parameters"]
      self.opPartTranCreation:bool = obj["opPartTranCreation"]
      pass

      """  output parameters  """  

class ProcessSplitJob_input:
   """ Required : 
   ipJobNum
   ipNewJobNum
   ipDueDate
   partTranCreation
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  The input jobnum to split.  """  
      self.ipNewJobNum:str = obj["ipNewJobNum"]
      """  The input jobnum to split to.  """  
      self.ipDueDate:str = obj["ipDueDate"]
      """  The input DueDate to split to.  """  
      self.partTranCreation:bool = obj["partTranCreation"]
      """  Flag to indicate if the split generates a PartTran record  """  
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

class ProcessSplitJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLegalNumberMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSplitJobTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSplitJobTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateJobProd_input:
   """ Required : 
   ipJobProdRowid
   ds
   """  
   def __init__(self, obj):
      self.ipJobProdRowid:str = obj["ipJobProdRowid"]
      """  The character rowid value of the JobProd to validate  """  
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

class ValidateJobProd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitJobTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

