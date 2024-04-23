import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARPIStatusChgSvc
# Description: AR Payment Instrument Status Change Service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ARPIStatusChgs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPIStatusChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPIStatusChgs
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs",headers=creds) as resp:
           return await resp.json()

async def post_ARPIStatusChgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPIStatusChgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPIStatusChgs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPIStatusChg item
   Description: Calls GetByID to retrieve the ARPIStatusChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPIStatusChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPIStatusChgs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPIStatusChg for the service
   Description: Calls UpdateExt to update ARPIStatusChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPIStatusChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPIStatusChgs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPIStatusChg item
   Description: Call UpdateExt to delete ARPIStatusChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPIStatusChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPIStatusChgs_Company_GroupID_HeadNum_ARPNDtls(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls",headers=creds) as resp:
           return await resp.json()

async def get_ARPIStatusChgs_Company_GroupID_HeadNum_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls",headers=creds) as resp:
           return await resp.json()

async def post_ARPNDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNDtl for the service
   Description: Calls UpdateExt to update ARPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNDtl item
   Description: Call UpdateExt to delete ARPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseARPNHead, whereClauseARPNDtl, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseARPNHead=" + whereClauseARPNHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNDtl=" + whereClauseARPNDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddSinglePI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddSinglePI
   Description: Add a single PI to the group
   OperationID: AddSinglePI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSinglePI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSinglePI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BankExportToProcessFolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BankExportToProcessFolder
   OperationID: BankExportToProcessFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BankExportToProcessFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankExportToProcessFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BankExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BankExport
   Description: Create Bank Export output file
   OperationID: BankExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BankExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteExportServerFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteExportServerFile
   Description: Delete server file.
   OperationID: DeleteExportServerFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteExportServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExportServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLastARPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLastARPNMove
   OperationID: DeleteLastARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLastARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLastARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupPIs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupPIs
   Description: Get Current ARPNHead records for the group
   OperationID: GetGroupPIs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupPIs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupPIs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByGroup
   Description: Get Current ARPNHead records by group
   OperationID: GetByGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByGroupHeadNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByGroupHeadNum
   Description: Get Current ARPNHead records by group
   OperationID: GetByGroupHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByGroupHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroupHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoCancelOnAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoCancelOnAccount
   Description: Undo credit Memo changes
   OperationID: UndoCancelOnAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoCancelOnAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoCancelOnAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessCancelOnAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessCancelOnAccount
   Description: Processes credit Memo
   OperationID: ProcessCancelOnAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessCancelOnAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessCancelOnAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveFromGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveFromGroup
   Description: Removes AR PN records from the current group
   OperationID: RemoveFromGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveFromGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectPI
   Description: Search Payment Instruments to add to group
   OperationID: SelectPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectPIData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectPIData
   Description: Select Payment Instruments to add to group
   OperationID: SelectPIData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectPIData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPIData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatusFromABR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatusFromABR
   Description: Change ARPN status from ABR
   OperationID: ChangeStatusFromABR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatusFromABR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatusFromABR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnDiscountingCashDateChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnDiscountingCashDateChange
   Description: This method should be called on Discounting Cash Date changing.
   OperationID: OnDiscountingCashDateChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnDiscountingCashDateChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountingCashDateChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnDiscountingChargeChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnDiscountingChargeChange
   Description: This method should be called on Discounting Change changing.
   OperationID: OnDiscountingChargeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnDiscountingChargeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountingChargeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnDiscountedAmountChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnDiscountedAmountChange
   Description: This method should be called on Discounted amount changing.
   OperationID: OnDiscountedAmountChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnDiscountedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the status change.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOptsFromABR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOptsFromABR
   Description: Returns the legal number generation options when called from ABR.
   OperationID: GetLegalNumGenOptsFromABR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOptsFromABR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOptsFromABR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePost
   Description: Ensure all data is ready to be posted.
   OperationID: PrePost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Discount Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Difference  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Discount Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Discount Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Discount Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.NewBalance:int = obj["NewBalance"]
      self.NetCash:int = obj["NetCash"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BillConNumber:int = obj["BillConNumber"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocSelfAssessTax:int = obj["DocSelfAssessTax"]
      self.DocWithholdTax:int = obj["DocWithholdTax"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.InvExchRate:int = obj["InvExchRate"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.PostToGL:bool = obj["PostToGL"]
      self.SelfAssessTax:int = obj["SelfAssessTax"]
      self.SoldToCustID:str = obj["SoldToCustID"]
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      self.WithholdTax:int = obj["WithholdTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.InvoicePosted:bool = obj["InvoicePosted"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
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




#########################################################################
# Custom Schemas:
#########################################################################
class AddSinglePI_input:
   """ Required : 
   piGroup
   piHeadNum
   piNewGroup
   piGrpStatus
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Header Group ID  """  
      self.piHeadNum:int = obj["piHeadNum"]
      """  Header Number  """  
      self.piNewGroup:str = obj["piNewGroup"]
      """  New Group ID  """  
      self.piGrpStatus:str = obj["piGrpStatus"]
      """  Group Status  """  
      pass

class AddSinglePI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

class AssignLegalNumber_input:
   """ Required : 
   ds
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Payment Instrument Head Number  """  
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class BankExportToProcessFolder_input:
   """ Required : 
   ipGroupID
   ipFileFormat
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipFileFormat:int = obj["ipFileFormat"]
      pass

class BankExportToProcessFolder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipOutRelativeFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class BankExport_input:
   """ Required : 
   ipGroupID
   ipFileFormat
   ipOutFileName
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipFileFormat:int = obj["ipFileFormat"]
      """  Output File Format  """  
      self.ipOutFileName:str = obj["ipOutFileName"]
      """  Output Filename  """  
      pass

class BankExport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipOutFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeStatusFromABR_input:
   """ Required : 
   ipGroupID
   ipCurGroupID
   ipHeadNum
   ipPIStatus
   ipTranDate
   ipLegalNumGenOpts
   ipTranDocTypeID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipCurGroupID:str = obj["ipCurGroupID"]
      """  Current Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  HeadNum  """  
      self.ipPIStatus:str = obj["ipPIStatus"]
      """  PIStatus  """  
      self.ipTranDate:str = obj["ipTranDate"]
      """  TranDate  """  
      self.ipLegalNumGenOpts:str = obj["ipLegalNumGenOpts"]
      """  Legal Number defaults  """  
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocType  """  
      pass

class ChangeStatusFromABR_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteExportServerFile_input:
   """ Required : 
   serverFile
   """  
   def __init__(self, obj):
      self.serverFile:str = obj["serverFile"]
      """  Server file path  """  
      pass

class DeleteExportServerFile_output:
   def __init__(self, obj):
      pass

class DeleteLastARPNMove_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      pass

class DeleteLastARPNMove_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARPIStatusChgTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNDtl:list[Erp_Tablesets_ARPNDtlRow] = obj["ARPNDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Discount Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Difference  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Discount Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Discount Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Discount Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.NewBalance:int = obj["NewBalance"]
      self.NetCash:int = obj["NetCash"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BillConNumber:int = obj["BillConNumber"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocSelfAssessTax:int = obj["DocSelfAssessTax"]
      self.DocWithholdTax:int = obj["DocWithholdTax"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.InvExchRate:int = obj["InvExchRate"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.PostToGL:bool = obj["PostToGL"]
      self.SelfAssessTax:int = obj["SelfAssessTax"]
      self.SoldToCustID:str = obj["SoldToCustID"]
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      self.WithholdTax:int = obj["WithholdTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.InvoicePosted:bool = obj["InvoicePosted"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadListTableset:
   def __init__(self, obj):
      self.ARPNHeadList:list[Erp_Tablesets_ARPNHeadListRow] = obj["ARPNHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
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

class Erp_Tablesets_LegalNumGenOptsTableset:
   def __init__(self, obj):
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtARPIStatusChgTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNDtl:list[Erp_Tablesets_ARPNDtlRow] = obj["ARPNDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByGroupHeadNum_input:
   """ Required : 
   ipGroup
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipGroup:str = obj["ipGroup"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  HeadNum  """  
      pass

class GetByGroupHeadNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByGroup_input:
   """ Required : 
   piGroup
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      pass

class GetByGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

class GetGroupPIs_input:
   """ Required : 
   piGroup
   piAutoBankRec
   piHeadNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      self.piAutoBankRec:bool = obj["piAutoBankRec"]
      """  The flag shows the PIs should be retrieved in AutoBankRec mode  """  
      self.piHeadNum:int = obj["piHeadNum"]
      """  HeadNum  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetGroupPIs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLegalNumGenOptsFromABR_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipStatusChgTranDocType
   ipTranDate
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Payment Instrument Head Number  """  
      self.ipStatusChgTranDocType:str = obj["ipStatusChgTranDocType"]
      """  Document Type for the status change  """  
      self.ipTranDate:str = obj["ipTranDate"]
      """  Transaction Date  """  
      pass

class GetLegalNumGenOptsFromABR_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class GetLegalNumGenOpts_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipStatusChgTranDocType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Payment Instrument Head Number  """  
      self.ipStatusChgTranDocType:str = obj["ipStatusChgTranDocType"]
      """  Document Type for the status change  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewARPNDtl_input:
   """ Required : 
   ds
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewARPNDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewARPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseARPNHead
   whereClauseARPNDtl
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseARPNHead:str = obj["whereClauseARPNHead"]
      self.whereClauseARPNDtl:str = obj["whereClauseARPNDtl"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class OnDiscountedAmountChange_input:
   """ Required : 
   discountedAmount
   ds
   """  
   def __init__(self, obj):
      self.discountedAmount:int = obj["discountedAmount"]
      """  Discounted Amount  """  
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

class OnDiscountedAmountChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnDiscountingCashDateChange_input:
   """ Required : 
   discountingCashDate
   ds
   """  
   def __init__(self, obj):
      self.discountingCashDate:str = obj["discountingCashDate"]
      """  Discounting Cash Date  """  
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

class OnDiscountingCashDateChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnDiscountingChargeChange_input:
   """ Required : 
   discountingCharge
   ds
   """  
   def __init__(self, obj):
      self.discountingCharge:int = obj["discountingCharge"]
      """  Discounting Charge  """  
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

class OnDiscountingChargeChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePost_input:
   """ Required : 
   piGroup
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      pass

class PrePost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.poRunGL:str = obj["parameters"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class ProcessCancelOnAccount_input:
   """ Required : 
   ipFiscalInfo
   inARPNHeadKey
   """  
   def __init__(self, obj):
      self.ipFiscalInfo:str = obj["ipFiscalInfo"]
      """  Fiscal Info  """  
      self.inARPNHeadKey:str = obj["inARPNHeadKey"]
      """  AR PI  """  
      pass

class ProcessCancelOnAccount_output:
   def __init__(self, obj):
      pass

class RemoveFromGroup_input:
   """ Required : 
   ds
   bClearDiscountingCharge
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      self.bClearDiscountingCharge:bool = obj["bClearDiscountingCharge"]
      """  If true then system should try to clear discounting charge data  """  
      pass

class RemoveFromGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectPIData_input:
   """ Required : 
   piGroup
   piGrpStatus
   piPIList
   ds
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      self.piGrpStatus:str = obj["piGrpStatus"]
      """  Group Status  """  
      self.piPIList:str = obj["piPIList"]
      """  PI List  """  
      self.ds:list[Erp_Tablesets_ARPNHeadListTableset] = obj["ds"]
      pass

class SelectPIData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

class SelectPI_input:
   """ Required : 
   targetBankAcctID
   piGroup
   piGrpStatus
   piFromDate
   piToDate
   piType
   piCustFilter
   piCurrencyFilter
   piStatusFilter
   ipCashBookNum
   """  
   def __init__(self, obj):
      self.targetBankAcctID:str = obj["targetBankAcctID"]
      """  Target BankID  """  
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      self.piGrpStatus:str = obj["piGrpStatus"]
      """  Group Status  """  
      self.piFromDate:str = obj["piFromDate"]
      """  From DueDate  """  
      self.piToDate:str = obj["piToDate"]
      """  To DueDate  """  
      self.piType:str = obj["piType"]
      """  PI Type  """  
      self.piCustFilter:str = obj["piCustFilter"]
      """  Customer Filter  """  
      self.piCurrencyFilter:str = obj["piCurrencyFilter"]
      """  Currency Filter  """  
      self.piStatusFilter:str = obj["piStatusFilter"]
      """  StatusFilter  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  CashBook  """  
      pass

class SelectPI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

class UndoCancelOnAccount_input:
   """ Required : 
   inARPNHeadKey
   """  
   def __init__(self, obj):
      self.inARPNHeadKey:str = obj["inARPNHeadKey"]
      """  AR PI  """  
      pass

class UndoCancelOnAccount_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARPIStatusChgTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARPIStatusChgTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group identifier.  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Payment Instrument Head Number.  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Indicates reason why legal number should be voided.  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIStatusChgTableset] = obj["returnObj"]
      pass

