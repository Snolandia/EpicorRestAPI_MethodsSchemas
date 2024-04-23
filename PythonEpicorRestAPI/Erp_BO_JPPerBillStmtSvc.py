import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JPPerBillStmtSvc
# Description: Japan Localization - Periodic Billing Statement Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBillStmts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPPerBillStmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPPerBillStmts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts",headers=creds) as resp:
           return await resp.json()

async def post_JPPerBillStmts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPPerBillStmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPPerBillStmt item
   Description: Calls GetByID to retrieve the JPPerBillStmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPPerBillStmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPPerBillStmt for the service
   Description: Calls UpdateExt to update JPPerBillStmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPPerBillStmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPPerBillStmts_Company_PerBillStmtGrpID(Company, PerBillStmtGrpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPPerBillStmt item
   Description: Call UpdateExt to delete JPPerBillStmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPPerBillStmt
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBillStmts_Company_PerBillStmtGrpID_PerBillStmtHeads(Company, PerBillStmtGrpID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PerBillStmtHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerBillStmtHeads1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/PerBillStmtHeads",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBillStmts_Company_PerBillStmtGrpID_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company, PerBillStmtGrpID, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillStmtHead item
   Description: Calls GetByID to retrieve the PerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtHead1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtHeads(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerBillStmtHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtHeads
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads",headers=creds) as resp:
           return await resp.json()

async def post_PerBillStmtHeads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company, PerBillStmtGrpID, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillStmtHead item
   Description: Calls GetByID to retrieve the PerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company, PerBillStmtGrpID, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerBillStmtHead for the service
   Description: Calls UpdateExt to update PerBillStmtHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company, PerBillStmtGrpID, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerBillStmtHead item
   Description: Call UpdateExt to delete PerBillStmtHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum_PerBillStmtPays(Company, PerBillStmtGrpID, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PerBillStmtPays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerBillStmtPays1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")/PerBillStmtPays",headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company, PerBillStmtGrpID, CustNum, StmtPayLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillStmtPay item
   Description: Calls GetByID to retrieve the PerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtPay1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtPays(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerBillStmtPays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtPays
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays",headers=creds) as resp:
           return await resp.json()

async def post_PerBillStmtPays(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtPays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company, PerBillStmtGrpID, CustNum, StmtPayLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillStmtPay item
   Description: Calls GetByID to retrieve the PerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company, PerBillStmtGrpID, CustNum, StmtPayLineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerBillStmtPay for the service
   Description: Calls UpdateExt to update PerBillStmtPay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param StmtPayLineNum: Desc: StmtPayLineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company, PerBillStmtGrpID, CustNum, StmtPayLineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerBillStmtPay item
   Description: Call UpdateExt to delete PerBillStmtPay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtPay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerBillStmtDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls",headers=creds) as resp:
           return await resp.json()

async def post_PerBillStmtDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company, PerBillStmtGrpID, CustNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillStmtDtl item
   Description: Calls GetByID to retrieve the PerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company, PerBillStmtGrpID, CustNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerBillStmtDtl for the service
   Description: Calls UpdateExt to update PerBillStmtDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company, PerBillStmtGrpID, CustNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerBillStmtDtl item
   Description: Call UpdateExt to delete PerBillStmtDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerBillStmtGrpID: Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePerBillStmtGrp, whereClausePerBillStmtHead, whereClausePerBillStmtDtl, whereClausePerBillStmtPay, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePerBillStmtGrp=" + whereClausePerBillStmtGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerBillStmtHead=" + whereClausePerBillStmtHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerBillStmtDtl=" + whereClausePerBillStmtDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerBillStmtPay=" + whereClausePerBillStmtPay
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomers
   Description: Syncronize the DueDate and Billing date HeadInvoice with the values of the  PerBillStmtDtl table.
   OperationID: GetCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustID
   Description: Receives CustId, returns CustNum
   OperationID: ValidateCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillStmtGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillStmtGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillStmtHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillStmtHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillStmtDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillStmtDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillStmtPay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillStmtPay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtPay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillStmtDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillStmtGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillStmtGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillStmtHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillStmtPayRow] = obj["value"]
      pass

class Erp_Tablesets_PerBillStmtDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Ready to Bill  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Synchronized:bool = obj["Synchronized"]
      """  Flag that let us know if the Dates are synchronized with the AR Invoice  """  
      self.DspInvoiceAmt:int = obj["DspInvoiceAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.InvcHeadTermsCode:str = obj["InvcHeadTermsCode"]
      self.InvcHeadInvoiceAmt:int = obj["InvcHeadInvoiceAmt"]
      self.InvcHeadCardMemberName:str = obj["InvcHeadCardMemberName"]
      self.InvcHeadBillingNumber:str = obj["InvcHeadBillingNumber"]
      self.InvcHeadInvoiceDate:str = obj["InvcHeadInvoiceDate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Ready to Bill  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartSumDate:str = obj["StartSumDate"]
      """  StartSumDate  """  
      self.EndSumDate:str = obj["EndSumDate"]
      """  EndSumDate  """  
      self.AmountToPay:int = obj["AmountToPay"]
      """  AmountToPay  """  
      self.CalcTaxGlb:bool = obj["CalcTaxGlb"]
      """  CalcTaxGlb  """  
      self.AdjInvoiceNum:int = obj["AdjInvoiceNum"]
      """  AdjInvoiceNum  """  
      self.CustID:str = obj["CustID"]
      self.dispBillingDate:str = obj["dispBillingDate"]
      """  Date when a company bills the customer  """  
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PerBillHeadDueDateCriteria:str = obj["PerBillHeadDueDateCriteria"]
      self.PerBillHeadPerBillTerms:int = obj["PerBillHeadPerBillTerms"]
      self.SummDayEndOfMonth:bool = obj["SummDayEndOfMonth"]
      self.SummDayTermsCode:str = obj["SummDayTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtPayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.StmtPayLineNum:int = obj["StmtPayLineNum"]
      """  StmtPayLineNum  """  
      self.PayGroupID:str = obj["PayGroupID"]
      """  PayGroupID  """  
      self.PayHeadNum:int = obj["PayHeadNum"]
      """  PayHeadNum  """  
      self.PayInvoiceNum:int = obj["PayInvoiceNum"]
      """  PayInvoiceNum  """  
      self.PayInvoiceRef:int = obj["PayInvoiceRef"]
      """  PayInvoiceRef  """  
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

class Erp_Tablesets_JPPerBillStmtTableset:
   def __init__(self, obj):
      self.PerBillStmtGrp:list[Erp_Tablesets_PerBillStmtGrpRow] = obj["PerBillStmtGrp"]
      self.PerBillStmtHead:list[Erp_Tablesets_PerBillStmtHeadRow] = obj["PerBillStmtHead"]
      self.PerBillStmtDtl:list[Erp_Tablesets_PerBillStmtDtlRow] = obj["PerBillStmtDtl"]
      self.PerBillStmtPay:list[Erp_Tablesets_PerBillStmtPayRow] = obj["PerBillStmtPay"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerBillStmtDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Ready to Bill  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Synchronized:bool = obj["Synchronized"]
      """  Flag that let us know if the Dates are synchronized with the AR Invoice  """  
      self.DspInvoiceAmt:int = obj["DspInvoiceAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.InvcHeadTermsCode:str = obj["InvcHeadTermsCode"]
      self.InvcHeadInvoiceAmt:int = obj["InvcHeadInvoiceAmt"]
      self.InvcHeadCardMemberName:str = obj["InvcHeadCardMemberName"]
      self.InvcHeadBillingNumber:str = obj["InvcHeadBillingNumber"]
      self.InvcHeadInvoiceDate:str = obj["InvcHeadInvoiceDate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtGrpListTableset:
   def __init__(self, obj):
      self.PerBillStmtGrpList:list[Erp_Tablesets_PerBillStmtGrpListRow] = obj["PerBillStmtGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerBillStmtGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Ready to Bill  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartSumDate:str = obj["StartSumDate"]
      """  StartSumDate  """  
      self.EndSumDate:str = obj["EndSumDate"]
      """  EndSumDate  """  
      self.AmountToPay:int = obj["AmountToPay"]
      """  AmountToPay  """  
      self.CalcTaxGlb:bool = obj["CalcTaxGlb"]
      """  CalcTaxGlb  """  
      self.AdjInvoiceNum:int = obj["AdjInvoiceNum"]
      """  AdjInvoiceNum  """  
      self.CustID:str = obj["CustID"]
      self.dispBillingDate:str = obj["dispBillingDate"]
      """  Date when a company bills the customer  """  
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PerBillHeadDueDateCriteria:str = obj["PerBillHeadDueDateCriteria"]
      self.PerBillHeadPerBillTerms:int = obj["PerBillHeadPerBillTerms"]
      self.SummDayEndOfMonth:bool = obj["SummDayEndOfMonth"]
      self.SummDayTermsCode:str = obj["SummDayTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillStmtPayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PerBillStmtGrpID:str = obj["PerBillStmtGrpID"]
      """  PerBillStmtGrpID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.StmtPayLineNum:int = obj["StmtPayLineNum"]
      """  StmtPayLineNum  """  
      self.PayGroupID:str = obj["PayGroupID"]
      """  PayGroupID  """  
      self.PayHeadNum:int = obj["PayHeadNum"]
      """  PayHeadNum  """  
      self.PayInvoiceNum:int = obj["PayInvoiceNum"]
      """  PayInvoiceNum  """  
      self.PayInvoiceRef:int = obj["PayInvoiceRef"]
      """  PayInvoiceRef  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtJPPerBillStmtTableset:
   def __init__(self, obj):
      self.PerBillStmtGrp:list[Erp_Tablesets_PerBillStmtGrpRow] = obj["PerBillStmtGrp"]
      self.PerBillStmtHead:list[Erp_Tablesets_PerBillStmtHeadRow] = obj["PerBillStmtHead"]
      self.PerBillStmtDtl:list[Erp_Tablesets_PerBillStmtDtlRow] = obj["PerBillStmtDtl"]
      self.PerBillStmtPay:list[Erp_Tablesets_PerBillStmtPayRow] = obj["PerBillStmtPay"]
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
      self.returnObj:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["returnObj"]
      pass

class GetCustomers_input:
   """ Required : 
   ipGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipGrpID:str = obj["ipGrpID"]
      """  Group ID  """  
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class GetCustomers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_PerBillStmtGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPerBillStmtDtl_input:
   """ Required : 
   ds
   perBillStmtGrpID
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewPerBillStmtDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerBillStmtGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class GetNewPerBillStmtGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerBillStmtHead_input:
   """ Required : 
   ds
   perBillStmtGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      pass

class GetNewPerBillStmtHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerBillStmtPay_input:
   """ Required : 
   ds
   perBillStmtGrpID
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      self.perBillStmtGrpID:str = obj["perBillStmtGrpID"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewPerBillStmtPay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePerBillStmtGrp
   whereClausePerBillStmtHead
   whereClausePerBillStmtDtl
   whereClausePerBillStmtPay
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerBillStmtGrp:str = obj["whereClausePerBillStmtGrp"]
      self.whereClausePerBillStmtHead:str = obj["whereClausePerBillStmtHead"]
      self.whereClausePerBillStmtDtl:str = obj["whereClausePerBillStmtDtl"]
      self.whereClausePerBillStmtPay:str = obj["whereClausePerBillStmtPay"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPPerBillStmtTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPPerBillStmtTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBillingDate_input:
   """ Required : 
   ipBillingDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillingDate:str = obj["ipBillingDate"]
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateBillingDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDueDate:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCustID_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  Customer ID  """  
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCustNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateDueDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

class ValidateReadyToBill_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillStmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

