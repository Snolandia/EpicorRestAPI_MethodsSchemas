import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JPAPPerBillStmtSvc
# Description: Japan Localization - Payment Proposal Statement Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBillStmts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmt item
   Description: Calls GetByID to retrieve the JPAPPerBillStmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBillStmt for the service
   Description: Calls UpdateExt to update JPAPPerBillStmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBillStmt item
   Description: Call UpdateExt to delete JPAPPerBillStmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmts_Company_PerBillStmtGrpID_JPAPPerBillStmtHeads(Company, PerBillStmtGrpID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JPAPPerBillStmtHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtHeads1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/JPAPPerBillStmtHeads",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmts_Company_PerBillStmtGrpID_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company, PerBillStmtGrpID, VendorNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtHead item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtHead1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmtHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtHeads
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBillStmtHeads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company, PerBillStmtGrpID, VendorNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtHead item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company, PerBillStmtGrpID, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBillStmtHead for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company, PerBillStmtGrpID, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBillStmtHead item
   Description: Call UpdateExt to delete JPAPPerBillStmtHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtDtls(Company, PerBillStmtGrpID, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JPAPPerBillStmtDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtDtls",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company, PerBillStmtGrpID, VendorNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtPays(Company, PerBillStmtGrpID, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JPAPPerBillStmtPays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtPays1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtPays",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company, PerBillStmtGrpID, VendorNum, StmtPayLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtPay item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtPay1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmtDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBillStmtDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company, PerBillStmtGrpID, VendorNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company, PerBillStmtGrpID, VendorNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBillStmtDtl for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company, PerBillStmtGrpID, VendorNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBillStmtDtl item
   Description: Call UpdateExt to delete JPAPPerBillStmtDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtPays(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmtPays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtPays
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBillStmtPays(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtPays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company, PerBillStmtGrpID, VendorNum, StmtPayLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtPay item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company, PerBillStmtGrpID, VendorNum, StmtPayLineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBillStmtPay for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtPay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company, PerBillStmtGrpID, VendorNum, StmtPayLineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBillStmtPay item
   Description: Call UpdateExt to delete JPAPPerBillStmtPay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJPAPPerBillStmtGrp, whereClauseJPAPPerBillStmtHead, whereClauseJPAPPerBillStmtDtl, whereClauseJPAPPerBillStmtPay, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJPAPPerBillStmtGrp=" + whereClauseJPAPPerBillStmtGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJPAPPerBillStmtHead=" + whereClauseJPAPPerBillStmtHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJPAPPerBillStmtDtl=" + whereClauseJPAPPerBillStmtDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJPAPPerBillStmtPay=" + whereClauseJPAPPerBillStmtPay
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(perBillStmtGrpID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "perBillStmtGrpID=" + perBillStmtGrpID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSuppliers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSuppliers
   Description: Synchronize the DueDate and Billing date HeadInvoice with the values of the  PerBillStmtDtl table.
   OperationID: GetSuppliers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBillingDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBillingDate
   OperationID: ValidateBillingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBillingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBillingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateVendorID
   Description: Validates Vendor ID
   OperationID: ValidateVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateVendorNum
   Description: Validates Vendor No
   OperationID: ValidateVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDueDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDueDate
   Description: Validate that the due date is not lower than the billing date.
   OperationID: ValidateDueDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateReadyToBill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateReadyToBill
   Description: Validate that all the invoices are syncronized before setting the customer to "ready to bill.
   OperationID: ValidateReadyToBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReadyToBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReadyToBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJPConsumptionTax(epicorHeaders = None):
   """  
   Summary: Invoke method CheckJPConsumptionTax
   Description: Check Japan Consumption Tax exists.
   OperationID: CheckJPConsumptionTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJPConsumptionTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillStmtGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillStmtGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillStmtHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillStmtHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillStmtDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillStmtDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillStmtPay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillStmtPay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtPay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillStmtDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillStmtGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillStmtGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillStmtHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillStmtPayRow] = obj["value"]
      pass

class Erp_Tablesets_JPAPPerBillStmtDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APInvHedInvoiceDate:str = obj["APInvHedInvoiceDate"]
      self.APInvHedInvoiceAmt:int = obj["APInvHedInvoiceAmt"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  ReadyToBill  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  SummarizationDay  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.StartSumDate:str = obj["StartSumDate"]
      """  StartSumDate  """  
      self.EndSumDate:str = obj["EndSumDate"]
      """  EndSumDate  """  
      self.AmountToPay:int = obj["AmountToPay"]
      """  AmountToPay  """  
      self.CalcTaxGlb:bool = obj["CalcTaxGlb"]
      """  CalcTaxGlb  """  
      self.AdjInvoiceNum:str = obj["AdjInvoiceNum"]
      """  AdjInvoiceNum  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DspBillingDate:str = obj["DspBillingDate"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.JPAPPerBillHeadDueDateCriteria:str = obj["JPAPPerBillHeadDueDateCriteria"]
      self.SummDayTermsCode:str = obj["SummDayTermsCode"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtPayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.StmtPayLineNum:int = obj["StmtPayLineNum"]
      """  StmtPayLineNum  """  
      self.PayHeadNum:int = obj["PayHeadNum"]
      """  PayHeadNum  """  
      self.PayInvoiceNum:str = obj["PayInvoiceNum"]
      """  PayInvoiceNum  """  
      self.PayVoided:bool = obj["PayVoided"]
      """  PayVoided  """  
      self.PayAPTranNo:int = obj["PayAPTranNo"]
      """  PayAPTranNo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckJPConsumptionTax_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   perBillStmtGrpID
   """  
   def __init__(self, obj):
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JPAPPerBillStmtDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APInvHedInvoiceDate:str = obj["APInvHedInvoiceDate"]
      self.APInvHedInvoiceAmt:int = obj["APInvHedInvoiceAmt"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtGrpListTableset:
   def __init__(self, obj):
      self.JPAPPerBillStmtGrpList:list[Erp_Tablesets_JPAPPerBillStmtGrpListRow] = obj["JPAPPerBillStmtGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JPAPPerBillStmtGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.BillingDate:str = obj["BillingDate"]
      """  BillingDate  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  SummarizationDate  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  ReadyToBill  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  SummarizationDay  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.StartSumDate:str = obj["StartSumDate"]
      """  StartSumDate  """  
      self.EndSumDate:str = obj["EndSumDate"]
      """  EndSumDate  """  
      self.AmountToPay:int = obj["AmountToPay"]
      """  AmountToPay  """  
      self.CalcTaxGlb:bool = obj["CalcTaxGlb"]
      """  CalcTaxGlb  """  
      self.AdjInvoiceNum:str = obj["AdjInvoiceNum"]
      """  AdjInvoiceNum  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DspBillingDate:str = obj["DspBillingDate"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.JPAPPerBillHeadDueDateCriteria:str = obj["JPAPPerBillHeadDueDateCriteria"]
      self.SummDayTermsCode:str = obj["SummDayTermsCode"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtPayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.StmtPayLineNum:int = obj["StmtPayLineNum"]
      """  StmtPayLineNum  """  
      self.PayHeadNum:int = obj["PayHeadNum"]
      """  PayHeadNum  """  
      self.PayInvoiceNum:str = obj["PayInvoiceNum"]
      """  PayInvoiceNum  """  
      self.PayVoided:bool = obj["PayVoided"]
      """  PayVoided  """  
      self.PayAPTranNo:int = obj["PayAPTranNo"]
      """  PayAPTranNo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillStmtTableset:
   def __init__(self, obj):
      self.JPAPPerBillStmtGrp:list[Erp_Tablesets_JPAPPerBillStmtGrpRow] = obj["JPAPPerBillStmtGrp"]
      self.JPAPPerBillStmtHead:list[Erp_Tablesets_JPAPPerBillStmtHeadRow] = obj["JPAPPerBillStmtHead"]
      self.JPAPPerBillStmtDtl:list[Erp_Tablesets_JPAPPerBillStmtDtlRow] = obj["JPAPPerBillStmtDtl"]
      self.JPAPPerBillStmtPay:list[Erp_Tablesets_JPAPPerBillStmtPayRow] = obj["JPAPPerBillStmtPay"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJPAPPerBillStmtTableset:
   def __init__(self, obj):
      self.JPAPPerBillStmtGrp:list[Erp_Tablesets_JPAPPerBillStmtGrpRow] = obj["JPAPPerBillStmtGrp"]
      self.JPAPPerBillStmtHead:list[Erp_Tablesets_JPAPPerBillStmtHeadRow] = obj["JPAPPerBillStmtHead"]
      self.JPAPPerBillStmtDtl:list[Erp_Tablesets_JPAPPerBillStmtDtlRow] = obj["JPAPPerBillStmtDtl"]
      self.JPAPPerBillStmtPay:list[Erp_Tablesets_JPAPPerBillStmtPayRow] = obj["JPAPPerBillStmtPay"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   perBillStmtGrpID
   """  
   def __init__(self, obj):
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillStmtGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillStmtDtl_input:
   """ Required : 
   ds
   perBillStmtGrpID
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewJPAPPerBillStmtDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillStmtGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class GetNewJPAPPerBillStmtGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillStmtHead_input:
   """ Required : 
   ds
   perBillStmtGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      pass

class GetNewJPAPPerBillStmtHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillStmtPay_input:
   """ Required : 
   ds
   perBillStmtGrpID
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewJPAPPerBillStmtPay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJPAPPerBillStmtGrp
   whereClauseJPAPPerBillStmtHead
   whereClauseJPAPPerBillStmtDtl
   whereClauseJPAPPerBillStmtPay
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJPAPPerBillStmtGrp:str = obj["whereClauseJPAPPerBillStmtGrp"]
      self.whereClauseJPAPPerBillStmtHead:str = obj["whereClauseJPAPPerBillStmtHead"]
      self.whereClauseJPAPPerBillStmtDtl:str = obj["whereClauseJPAPPerBillStmtDtl"]
      self.whereClauseJPAPPerBillStmtPay:str = obj["whereClauseJPAPPerBillStmtPay"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSuppliers_input:
   """ Required : 
   ipGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipGrpID:str = obj["ipGrpID"]
      """  Group ID  """  
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class GetSuppliers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPAPPerBillStmtTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPAPPerBillStmtTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBillingDate_input:
   """ Required : 
   ipBillingDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillingDate:str = obj["ipBillingDate"]
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateBillingDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDueDate:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateDueDate_input:
   """ Required : 
   ipDueDate
   ds
   """  
   def __init__(self, obj):
      self.ipDueDate:str = obj["ipDueDate"]
      """  Proposed DueDate  """  
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateDueDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateReadyToBill_input:
   """ Required : 
   ipReadyToBill
   ds
   """  
   def __init__(self, obj):
      self.ipReadyToBill:bool = obj["ipReadyToBill"]
      """  Proposed Ready To Bill status  """  
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateReadyToBill_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateVendorID_input:
   """ Required : 
   ipVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipVendorID:str = obj["ipVendorID"]
      """  Vendor ID  """  
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateVendorNum_input:
   """ Required : 
   ipVendorNum
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor No  """  
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

