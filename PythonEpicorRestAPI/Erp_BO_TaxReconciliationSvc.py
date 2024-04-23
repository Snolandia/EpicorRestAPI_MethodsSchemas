import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxReconciliationSvc
# Description: Procedure used for reconciling TaxSvcHead records and the tax integration
service records.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxReconciliations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxReconciliations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations",headers=creds) as resp:
           return await resp.json()

async def post_TaxReconciliations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxReconciliations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations_Company_TaxSvcID(Company, TaxSvcID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxReconciliation item
   Description: Calls GetByID to retrieve the TaxReconciliation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxReconciliation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxReconciliations_Company_TaxSvcID(Company, TaxSvcID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxReconciliation for the service
   Description: Calls UpdateExt to update TaxReconciliation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxReconciliation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxReconciliations_Company_TaxSvcID(Company, TaxSvcID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxReconciliation item
   Description: Call UpdateExt to delete TaxReconciliation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxReconciliation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations_Company_TaxSvcID_TaxSvcDetails(Company, TaxSvcID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")/TaxSvcDetails",headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations_Company_TaxSvcID_TaxSvcDetails_Company_TaxSvcID_TCNo(Company, TaxSvcID, TCNo, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcDetail item
   Description: Calls GetByID to retrieve the TaxSvcDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations_Company_TaxSvcID_TaxSvcMessages(Company, TaxSvcID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcMessages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcMessages1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")/TaxSvcMessages",headers=creds) as resp:
           return await resp.json()

async def get_TaxReconciliations_Company_TaxSvcID_TaxSvcMessages_Company_TaxSvcID_Sequence(Company, TaxSvcID, Sequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcMessage item
   Description: Calls GetByID to retrieve the TaxSvcMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcMessage1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxReconciliations(" + Company + "," + TaxSvcID + ")/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcDetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails",headers=creds) as resp:
           return await resp.json()

async def post_TaxSvcDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcDetails_Company_TaxSvcID_TCNo(Company, TaxSvcID, TCNo, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcDetail item
   Description: Calls GetByID to retrieve the TaxSvcDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxSvcDetails_Company_TaxSvcID_TCNo(Company, TaxSvcID, TCNo, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxSvcDetail for the service
   Description: Calls UpdateExt to update TaxSvcDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxSvcDetails_Company_TaxSvcID_TCNo(Company, TaxSvcID, TCNo, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxSvcDetail item
   Description: Call UpdateExt to delete TaxSvcDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcDetails_Company_TaxSvcID_TCNo_TaxSvcJurDtls(Company, TaxSvcID, TCNo, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcJurDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcJurDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcJurDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")/TaxSvcJurDtls",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcDetails_Company_TaxSvcID_TCNo_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company, TaxSvcID, TCNo, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcJurDtl item
   Description: Calls GetByID to retrieve the TaxSvcJurDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcJurDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcJurDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcJurDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcJurDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcJurDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcJurDtls",headers=creds) as resp:
           return await resp.json()

async def post_TaxSvcJurDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcJurDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcJurDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company, TaxSvcID, TCNo, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcJurDtl item
   Description: Calls GetByID to retrieve the TaxSvcJurDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcJurDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company, TaxSvcID, TCNo, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxSvcJurDtl for the service
   Description: Calls UpdateExt to update TaxSvcJurDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcJurDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company, TaxSvcID, TCNo, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxSvcJurDtl item
   Description: Call UpdateExt to delete TaxSvcJurDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcJurDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param TCNo: Desc: TCNo   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcMessages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcMessages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcMessages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcMessages",headers=creds) as resp:
           return await resp.json()

async def post_TaxSvcMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcMessages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcMessages_Company_TaxSvcID_Sequence(Company, TaxSvcID, Sequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcMessage item
   Description: Calls GetByID to retrieve the TaxSvcMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcMessage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxSvcMessages_Company_TaxSvcID_Sequence(Company, TaxSvcID, Sequence, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxSvcMessage for the service
   Description: Calls UpdateExt to update TaxSvcMessage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcMessage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxSvcMessages_Company_TaxSvcID_Sequence(Company, TaxSvcID, Sequence, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxSvcMessage item
   Description: Call UpdateExt to delete TaxSvcMessage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcMessage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxSvcID: Desc: TaxSvcID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxSvcHead, whereClauseTaxSvcDetail, whereClauseTaxSvcJurDtl, whereClauseTaxSvcMessages, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTaxSvcHead=" + whereClauseTaxSvcHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxSvcDetail=" + whereClauseTaxSvcDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxSvcJurDtl=" + whereClauseTaxSvcJurDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxSvcMessages=" + whereClauseTaxSvcMessages
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxSvcID, epicorHeaders = None):
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
   params += "taxSvcID=" + taxSvcID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAllActionCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAllActionCodes
   Description: Purpose: To return a list of all possible Action codes and descriptions to the
UI.
Parameters: AllResultCodes - delimited list of Action Codes and Descriptions
Notes:
   OperationID: GetAllActionCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllActionCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetLastDocID(epicorHeaders = None):
   """  
   Summary: Invoke method GetLastDocID
   Description: Get the last doc id from taxsvcconfig..
   OperationID: GetLastDocID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLastDocID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTaxHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxHistory
   Description: Deprecated, use GetTaxHistoryByDateRange to specify a date range.
This methods will only retrieve today's records.
   OperationID: GetTaxHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxHistoryByDateRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxHistoryByDateRange
   Description: Calls avalara ReconcileTaxHistory function to retrieve tax details
Updates TaxSvcHead Tax Connect History fields prefixed by TCH
   OperationID: GetTaxHistoryByDateRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxHistoryByDateRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxHistoryByDateRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofAction
   Description: Called when the user chooses a new action.
   OperationID: OnChangeofAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformReconciliation(epicorHeaders = None):
   """  
   Summary: Invoke method PerformReconciliation
   Description: Process TaxSvcHead records of type SalesInvoice/ReturnInvoice with an action assigned different from N (None)
It uses Lib.ProcessTaxes Avalara methods for Post/Commit/Cancel
For Get it uses CalcTaxes and ProcessAndUpdateTaxes methods
   OperationID: PerformReconciliation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformReconciliation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetHistDates(epicorHeaders = None):
   """  
   Summary: Invoke method GetHistDates
   Description: Get default date rage for GetHistory.
   OperationID: GetHistDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHistDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcJurDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcJurDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcJurDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcJurDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcJurDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcMessages
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxReconciliationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcJurDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcMessagesRow] = obj["value"]
      pass

class Erp_Tablesets_TaxSvcDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Order  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.LineNum:int = obj["LineNum"]
      """  Invoice or Order Line Number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with this tax detail  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity for this line item  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Price of this item  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Quantity x Unit Price  """  
      self.TaxableAmount:int = obj["TaxableAmount"]
      """  Amount of this line item that can be taxec  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Amount of tax for this line item  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.TaxCategory:str = obj["TaxCategory"]
      """  Tax Category  """  
      self.FromAddress1:str = obj["FromAddress1"]
      """  Address item was shipped from  """  
      self.FromAddress2:str = obj["FromAddress2"]
      """  Address item was shipped from  """  
      self.FromAddress3:str = obj["FromAddress3"]
      """  Address item was shipped from  """  
      self.FromCity:str = obj["FromCity"]
      """  City item was shipped from  """  
      self.FromState:str = obj["FromState"]
      """  State item was shipped from  """  
      self.FromZip:str = obj["FromZip"]
      """  Postal Code or zip code item was shipped from  """  
      self.FromCountry:str = obj["FromCountry"]
      """  Country item was shipped from  """  
      self.ToAddress1:str = obj["ToAddress1"]
      """  Address item was shipped TO  """  
      self.ToAddress2:str = obj["ToAddress2"]
      """  Address item was shipped to  """  
      self.ToAddress3:str = obj["ToAddress3"]
      """  Address item was shipped to  """  
      self.ToCity:str = obj["ToCity"]
      """  City item was shipped to  """  
      self.ToState:str = obj["ToState"]
      """  State item was shipped to  """  
      self.ToZip:str = obj["ToZip"]
      """  Postal Code or zip code item was shipped to  """  
      self.ToCountry:str = obj["ToCountry"]
      """  Country item was shipped to  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax region used to compute taxes.  """  
      self.DocID:int = obj["DocID"]
      """  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  """  
      self.TCNo:str = obj["TCNo"]
      """  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  """  
      self.TCRate:int = obj["TCRate"]
      """  TaxLine.Rate from GetTax call  """  
      self.TCHRate:int = obj["TCHRate"]
      """  TaxLine.Rate from GetTaxHistory call  """  
      self.TCTax:int = obj["TCTax"]
      """  TaxLine.Tax from GetTax call  """  
      self.TCHTax:int = obj["TCHTax"]
      """  TaxLine.Tax from GetTaxHistory call  """  
      self.TCTaxability:bool = obj["TCTaxability"]
      """  TaxLine.Taxability from GetTax call  """  
      self.TCHTaxability:bool = obj["TCHTaxability"]
      """  TaxLine.Taxability from GetTaxHistory call  """  
      self.TCTaxable:int = obj["TCTaxable"]
      """  TaxLine.Taxable from GetTax call  """  
      self.TCHTaxable:int = obj["TCHTaxable"]
      """  TaxLine.Taxable from GetTaxHistory call  """  
      self.TCTaxCode:str = obj["TCTaxCode"]
      """  TaxLine.TaxCode from GetTax call  """  
      self.TCHTaxCode:str = obj["TCHTaxCode"]
      """  TaxLine.TaxCode from GetTaxHistory call  """  
      self.ItemSeq:int = obj["ItemSeq"]
      """  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCategoryDescription:str = obj["TaxCategoryDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Orders  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.DocDate:str = obj["DocDate"]
      """  Document Date  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number  """  
      self.DocCodes:str = obj["DocCodes"]
      """  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  """  
      self.DocState:str = obj["DocState"]
      """  Posted / Unposted  """  
      self.RemoteState:str = obj["RemoteState"]
      """  Saved / Posted / Committed / Cancelled  """  
      self.TotalAmount:int = obj["TotalAmount"]
      """  Sum of taxable amounts  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Sum of tax amounts  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """  Sum of all line discounts  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  """  
      self.DocType:int = obj["DocType"]
      """  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  """  
      self.DocID:int = obj["DocID"]
      """  The unique id assigned by the tax service. Returned by the tax service.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Designates the document currency display symbol for the Epicor invoice Doc currency code  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.DateCreated:str = obj["DateCreated"]
      """  The date the TaxSvcHead entry was created  """  
      self.TimeCreated:int = obj["TimeCreated"]
      """  The time this entry was created.  """  
      self.TCHDocCode:str = obj["TCHDocCode"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.TCHRemoteState:str = obj["TCHRemoteState"]
      """   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  """  
      self.TCHTotalAmount:int = obj["TCHTotalAmount"]
      """  TotalAmount from ReconcileTaxHistoryCall  """  
      self.TCHTotalDiscount:int = obj["TCHTotalDiscount"]
      """  TotalDiscount from ReconcileTaxHistory call  """  
      self.TCHTotalTax:int = obj["TCHTotalTax"]
      """  TotalTax from ReconcileTaxHistory call.  """  
      self.ResultCode:str = obj["ResultCode"]
      """   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.TCHDocDate:str = obj["TCHDocDate"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.Action:str = obj["Action"]
      """   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.LastReconAction:str = obj["LastReconAction"]
      """   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailableActionOptions:str = obj["AvailableActionOptions"]
      """  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  """  
      self.ActionDescription:str = obj["ActionDescription"]
      """  ActionDescription  """  
      self.LastReconActionDesc:str = obj["LastReconActionDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Orders  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.DocDate:str = obj["DocDate"]
      """  Document Date  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number  """  
      self.DocCodes:str = obj["DocCodes"]
      """  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  """  
      self.DocState:str = obj["DocState"]
      """  Posted / Unposted  """  
      self.RemoteState:str = obj["RemoteState"]
      """  Saved / Posted / Committed / Cancelled  """  
      self.TotalAmount:int = obj["TotalAmount"]
      """  Sum of taxable amounts  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Sum of tax amounts  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """  Sum of all line discounts  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  """  
      self.DocType:int = obj["DocType"]
      """  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  """  
      self.DocID:int = obj["DocID"]
      """  The unique id assigned by the tax service. Returned by the tax service.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Designates the document currency display symbol for the Epicor invoice Doc currency code  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.DateCreated:str = obj["DateCreated"]
      """  The date the TaxSvcHead entry was created  """  
      self.TimeCreated:int = obj["TimeCreated"]
      """  The time this entry was created.  """  
      self.TCHDocCode:str = obj["TCHDocCode"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.TCHRemoteState:str = obj["TCHRemoteState"]
      """   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  """  
      self.TCHTotalAmount:int = obj["TCHTotalAmount"]
      """  TotalAmount from ReconcileTaxHistoryCall  """  
      self.TCHTotalDiscount:int = obj["TCHTotalDiscount"]
      """  TotalDiscount from ReconcileTaxHistory call  """  
      self.TCHTotalTax:int = obj["TCHTotalTax"]
      """  TotalTax from ReconcileTaxHistory call.  """  
      self.ResultCode:str = obj["ResultCode"]
      """   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.TCHDocDate:str = obj["TCHDocDate"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.Action:str = obj["Action"]
      """   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.LastReconAction:str = obj["LastReconAction"]
      """   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailableActionOptions:str = obj["AvailableActionOptions"]
      """  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  """  
      self.ActionDescription:str = obj["ActionDescription"]
      """  ActionDescription  """  
      self.LastReconActionDesc:str = obj["LastReconActionDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcJurDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.LineNum:int = obj["LineNum"]
      """  Invoice, Quote or Order Line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with this tax detail, for other types it will be zero.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence to keep the key unique per TaxSvcID, LineNum, OrderRelNum because there can be multiple jurisdiction tax details for each document/Line/Release combination.  """  
      self.TaxableAmount:int = obj["TaxableAmount"]
      """  From TaxDetail Base, the taxable amount. In Doc currency.  """  
      self.JurisCode:str = obj["JurisCode"]
      """  Jurisdiction Code for the taxing jurisdiction from GetTax call  """  
      self.JurisName:str = obj["JurisName"]
      """  Jurisdiction name returned by GetTax call.  """  
      self.JurisType:str = obj["JurisType"]
      """   Jurisdiction Type from GetTax call describes the jurisdiction for which a particular tax is applied to a document.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  """  
      self.Percent:int = obj["Percent"]
      """  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTax call  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTax call. In Doc currency.  """  
      self.TaxType:str = obj["TaxType"]
      """   TaxDetail.Tax type returned by GetTax call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  """  
      self.DocID:int = obj["DocID"]
      """  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  """  
      self.TCNo:str = obj["TCNo"]
      """  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  """  
      self.TCHTaxableAmount:int = obj["TCHTaxableAmount"]
      """  From TaxDetail Base, the taxable amount from GetTaxHistory call. In Doc currency.  """  
      self.TCHJurisCode:str = obj["TCHJurisCode"]
      """  Jurisdiction Code for the taxing jurisdiction from GetTaxHistory call  """  
      self.TCHJurisName:str = obj["TCHJurisName"]
      """  Jurisdiction name returned by GetTaxHistory call.  """  
      self.TCHJurisType:str = obj["TCHJurisType"]
      """   Jurisdiction Type from GetTaxHistory call.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  """  
      self.TCHPercent:int = obj["TCHPercent"]
      """  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTaxHistory call  """  
      self.TCHTaxAmt:int = obj["TCHTaxAmt"]
      """  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTaxHistory call. In Doc currency.  """  
      self.TCHTaxType:str = obj["TCHTaxType"]
      """   TaxDetail.Tax type returned by GetTaxHistory call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  """  
      self.ItemSeq:int = obj["ItemSeq"]
      """  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the related invoice.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcMessagesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum or InvoiceNum or QuoteNum'. Depending on the type, where Type is O=order, Q = quote and I = invoice. Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc. Used to link TaxSvcMessages to TaxSvcHead  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence of TaxSvcMessage  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Order  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number of item of the invoice or sales order  """  
      self.DocLineNum:int = obj["DocLineNum"]
      """  Line number of item in remote tax system  """  
      self.Detail:str = obj["Detail"]
      """  Detail of the message  """  
      self.HelpLink:str = obj["HelpLink"]
      """  URL of help page for this messag  """  
      self.Severity:str = obj["Severity"]
      """  Success, Warning, Error, Exception  """  
      self.Summary:str = obj["Summary"]
      """  Summary of the message  """  
      self.DocID:int = obj["DocID"]
      """  Unique identifier in remote tax system  """  
      self.Name:str = obj["Name"]
      """  Name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message is referring to  """  
      self.Source:str = obj["Source"]
      """  Source of the message  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with the message.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   taxSvcID
   """  
   def __init__(self, obj):
      self.taxSvcID:str = obj["taxSvcID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxReconciliationTableset:
   def __init__(self, obj):
      self.TaxSvcHead:list[Erp_Tablesets_TaxSvcHeadRow] = obj["TaxSvcHead"]
      self.TaxSvcDetail:list[Erp_Tablesets_TaxSvcDetailRow] = obj["TaxSvcDetail"]
      self.TaxSvcJurDtl:list[Erp_Tablesets_TaxSvcJurDtlRow] = obj["TaxSvcJurDtl"]
      self.TaxSvcMessages:list[Erp_Tablesets_TaxSvcMessagesRow] = obj["TaxSvcMessages"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxSvcDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Order  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.LineNum:int = obj["LineNum"]
      """  Invoice or Order Line Number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with this tax detail  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity for this line item  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Price of this item  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Quantity x Unit Price  """  
      self.TaxableAmount:int = obj["TaxableAmount"]
      """  Amount of this line item that can be taxec  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Amount of tax for this line item  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.TaxCategory:str = obj["TaxCategory"]
      """  Tax Category  """  
      self.FromAddress1:str = obj["FromAddress1"]
      """  Address item was shipped from  """  
      self.FromAddress2:str = obj["FromAddress2"]
      """  Address item was shipped from  """  
      self.FromAddress3:str = obj["FromAddress3"]
      """  Address item was shipped from  """  
      self.FromCity:str = obj["FromCity"]
      """  City item was shipped from  """  
      self.FromState:str = obj["FromState"]
      """  State item was shipped from  """  
      self.FromZip:str = obj["FromZip"]
      """  Postal Code or zip code item was shipped from  """  
      self.FromCountry:str = obj["FromCountry"]
      """  Country item was shipped from  """  
      self.ToAddress1:str = obj["ToAddress1"]
      """  Address item was shipped TO  """  
      self.ToAddress2:str = obj["ToAddress2"]
      """  Address item was shipped to  """  
      self.ToAddress3:str = obj["ToAddress3"]
      """  Address item was shipped to  """  
      self.ToCity:str = obj["ToCity"]
      """  City item was shipped to  """  
      self.ToState:str = obj["ToState"]
      """  State item was shipped to  """  
      self.ToZip:str = obj["ToZip"]
      """  Postal Code or zip code item was shipped to  """  
      self.ToCountry:str = obj["ToCountry"]
      """  Country item was shipped to  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax region used to compute taxes.  """  
      self.DocID:int = obj["DocID"]
      """  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  """  
      self.TCNo:str = obj["TCNo"]
      """  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  """  
      self.TCRate:int = obj["TCRate"]
      """  TaxLine.Rate from GetTax call  """  
      self.TCHRate:int = obj["TCHRate"]
      """  TaxLine.Rate from GetTaxHistory call  """  
      self.TCTax:int = obj["TCTax"]
      """  TaxLine.Tax from GetTax call  """  
      self.TCHTax:int = obj["TCHTax"]
      """  TaxLine.Tax from GetTaxHistory call  """  
      self.TCTaxability:bool = obj["TCTaxability"]
      """  TaxLine.Taxability from GetTax call  """  
      self.TCHTaxability:bool = obj["TCHTaxability"]
      """  TaxLine.Taxability from GetTaxHistory call  """  
      self.TCTaxable:int = obj["TCTaxable"]
      """  TaxLine.Taxable from GetTax call  """  
      self.TCHTaxable:int = obj["TCHTaxable"]
      """  TaxLine.Taxable from GetTaxHistory call  """  
      self.TCTaxCode:str = obj["TCTaxCode"]
      """  TaxLine.TaxCode from GetTax call  """  
      self.TCHTaxCode:str = obj["TCHTaxCode"]
      """  TaxLine.TaxCode from GetTaxHistory call  """  
      self.ItemSeq:int = obj["ItemSeq"]
      """  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCategoryDescription:str = obj["TaxCategoryDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Orders  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.DocDate:str = obj["DocDate"]
      """  Document Date  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number  """  
      self.DocCodes:str = obj["DocCodes"]
      """  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  """  
      self.DocState:str = obj["DocState"]
      """  Posted / Unposted  """  
      self.RemoteState:str = obj["RemoteState"]
      """  Saved / Posted / Committed / Cancelled  """  
      self.TotalAmount:int = obj["TotalAmount"]
      """  Sum of taxable amounts  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Sum of tax amounts  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """  Sum of all line discounts  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  """  
      self.DocType:int = obj["DocType"]
      """  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  """  
      self.DocID:int = obj["DocID"]
      """  The unique id assigned by the tax service. Returned by the tax service.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Designates the document currency display symbol for the Epicor invoice Doc currency code  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.DateCreated:str = obj["DateCreated"]
      """  The date the TaxSvcHead entry was created  """  
      self.TimeCreated:int = obj["TimeCreated"]
      """  The time this entry was created.  """  
      self.TCHDocCode:str = obj["TCHDocCode"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.TCHRemoteState:str = obj["TCHRemoteState"]
      """   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  """  
      self.TCHTotalAmount:int = obj["TCHTotalAmount"]
      """  TotalAmount from ReconcileTaxHistoryCall  """  
      self.TCHTotalDiscount:int = obj["TCHTotalDiscount"]
      """  TotalDiscount from ReconcileTaxHistory call  """  
      self.TCHTotalTax:int = obj["TCHTotalTax"]
      """  TotalTax from ReconcileTaxHistory call.  """  
      self.ResultCode:str = obj["ResultCode"]
      """   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.TCHDocDate:str = obj["TCHDocDate"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.Action:str = obj["Action"]
      """   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.LastReconAction:str = obj["LastReconAction"]
      """   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailableActionOptions:str = obj["AvailableActionOptions"]
      """  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  """  
      self.ActionDescription:str = obj["ActionDescription"]
      """  ActionDescription  """  
      self.LastReconActionDesc:str = obj["LastReconActionDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcHeadListTableset:
   def __init__(self, obj):
      self.TaxSvcHeadList:list[Erp_Tablesets_TaxSvcHeadListRow] = obj["TaxSvcHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxSvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Orders  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice or Credit Memo  """  
      self.DocDate:str = obj["DocDate"]
      """  Document Date  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number  """  
      self.DocCodes:str = obj["DocCodes"]
      """  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  """  
      self.DocState:str = obj["DocState"]
      """  Posted / Unposted  """  
      self.RemoteState:str = obj["RemoteState"]
      """  Saved / Posted / Committed / Cancelled  """  
      self.TotalAmount:int = obj["TotalAmount"]
      """  Sum of taxable amounts  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Sum of tax amounts  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """  Sum of all line discounts  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  """  
      self.DocType:int = obj["DocType"]
      """  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  """  
      self.DocID:int = obj["DocID"]
      """  The unique id assigned by the tax service. Returned by the tax service.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Designates the document currency display symbol for the Epicor invoice Doc currency code  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.DateCreated:str = obj["DateCreated"]
      """  The date the TaxSvcHead entry was created  """  
      self.TimeCreated:int = obj["TimeCreated"]
      """  The time this entry was created.  """  
      self.TCHDocCode:str = obj["TCHDocCode"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.TCHRemoteState:str = obj["TCHRemoteState"]
      """   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  """  
      self.TCHTotalAmount:int = obj["TCHTotalAmount"]
      """  TotalAmount from ReconcileTaxHistoryCall  """  
      self.TCHTotalDiscount:int = obj["TCHTotalDiscount"]
      """  TotalDiscount from ReconcileTaxHistory call  """  
      self.TCHTotalTax:int = obj["TCHTotalTax"]
      """  TotalTax from ReconcileTaxHistory call.  """  
      self.ResultCode:str = obj["ResultCode"]
      """   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.TCHDocDate:str = obj["TCHDocDate"]
      """  DocDate from ReconcileTaxHistory call  """  
      self.Action:str = obj["Action"]
      """   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.LastReconAction:str = obj["LastReconAction"]
      """   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailableActionOptions:str = obj["AvailableActionOptions"]
      """  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  """  
      self.ActionDescription:str = obj["ActionDescription"]
      """  ActionDescription  """  
      self.LastReconActionDesc:str = obj["LastReconActionDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcJurDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.LineNum:int = obj["LineNum"]
      """  Invoice, Quote or Order Line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with this tax detail, for other types it will be zero.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence to keep the key unique per TaxSvcID, LineNum, OrderRelNum because there can be multiple jurisdiction tax details for each document/Line/Release combination.  """  
      self.TaxableAmount:int = obj["TaxableAmount"]
      """  From TaxDetail Base, the taxable amount. In Doc currency.  """  
      self.JurisCode:str = obj["JurisCode"]
      """  Jurisdiction Code for the taxing jurisdiction from GetTax call  """  
      self.JurisName:str = obj["JurisName"]
      """  Jurisdiction name returned by GetTax call.  """  
      self.JurisType:str = obj["JurisType"]
      """   Jurisdiction Type from GetTax call describes the jurisdiction for which a particular tax is applied to a document.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  """  
      self.Percent:int = obj["Percent"]
      """  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTax call  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTax call. In Doc currency.  """  
      self.TaxType:str = obj["TaxType"]
      """   TaxDetail.Tax type returned by GetTax call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  """  
      self.DocID:int = obj["DocID"]
      """  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  """  
      self.TCNo:str = obj["TCNo"]
      """  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  """  
      self.TCHTaxableAmount:int = obj["TCHTaxableAmount"]
      """  From TaxDetail Base, the taxable amount from GetTaxHistory call. In Doc currency.  """  
      self.TCHJurisCode:str = obj["TCHJurisCode"]
      """  Jurisdiction Code for the taxing jurisdiction from GetTaxHistory call  """  
      self.TCHJurisName:str = obj["TCHJurisName"]
      """  Jurisdiction name returned by GetTaxHistory call.  """  
      self.TCHJurisType:str = obj["TCHJurisType"]
      """   Jurisdiction Type from GetTaxHistory call.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  """  
      self.TCHPercent:int = obj["TCHPercent"]
      """  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTaxHistory call  """  
      self.TCHTaxAmt:int = obj["TCHTaxAmt"]
      """  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTaxHistory call. In Doc currency.  """  
      self.TCHTaxType:str = obj["TCHTaxType"]
      """   TaxDetail.Tax type returned by GetTaxHistory call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  """  
      self.ItemSeq:int = obj["ItemSeq"]
      """  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the related invoice.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcMessagesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum or InvoiceNum or QuoteNum'. Depending on the type, where Type is O=order, Q = quote and I = invoice. Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc. Used to link TaxSvcMessages to TaxSvcHead  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence of TaxSvcMessage  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Link to Sales Order  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Link to Invoice  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number of item of the invoice or sales order  """  
      self.DocLineNum:int = obj["DocLineNum"]
      """  Line number of item in remote tax system  """  
      self.Detail:str = obj["Detail"]
      """  Detail of the message  """  
      self.HelpLink:str = obj["HelpLink"]
      """  URL of help page for this messag  """  
      self.Severity:str = obj["Severity"]
      """  Success, Warning, Error, Exception  """  
      self.Summary:str = obj["Summary"]
      """  Summary of the message  """  
      self.DocID:int = obj["DocID"]
      """  Unique identifier in remote tax system  """  
      self.Name:str = obj["Name"]
      """  Name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message is referring to  """  
      self.Source:str = obj["Source"]
      """  Source of the message  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Link to Quote  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  For SO, the release number associated with the message.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number sent to Tax Connect  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtTaxReconciliationTableset:
   def __init__(self, obj):
      self.TaxSvcHead:list[Erp_Tablesets_TaxSvcHeadRow] = obj["TaxSvcHead"]
      self.TaxSvcDetail:list[Erp_Tablesets_TaxSvcDetailRow] = obj["TaxSvcDetail"]
      self.TaxSvcJurDtl:list[Erp_Tablesets_TaxSvcJurDtlRow] = obj["TaxSvcJurDtl"]
      self.TaxSvcMessages:list[Erp_Tablesets_TaxSvcMessagesRow] = obj["TaxSvcMessages"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAllActionCodes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.AllResultCodes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   taxSvcID
   """  
   def __init__(self, obj):
      self.taxSvcID:str = obj["taxSvcID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxReconciliationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxReconciliationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxReconciliationTableset] = obj["returnObj"]
      pass

class GetHistDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.histStartDate:str = obj["parameters"]
      self.histEndDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLastDocID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lastDocID:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_TaxSvcHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxSvcDetail_input:
   """ Required : 
   ds
   taxSvcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      self.taxSvcID:str = obj["taxSvcID"]
      pass

class GetNewTaxSvcDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxSvcHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

class GetNewTaxSvcHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxSvcJurDtl_input:
   """ Required : 
   ds
   taxSvcID
   tcNo
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      self.taxSvcID:str = obj["taxSvcID"]
      self.tcNo:str = obj["tcNo"]
      pass

class GetNewTaxSvcJurDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxSvcMessages_input:
   """ Required : 
   ds
   taxSvcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      self.taxSvcID:str = obj["taxSvcID"]
      pass

class GetNewTaxSvcMessages_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxSvcHead
   whereClauseTaxSvcDetail
   whereClauseTaxSvcJurDtl
   whereClauseTaxSvcMessages
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxSvcHead:str = obj["whereClauseTaxSvcHead"]
      self.whereClauseTaxSvcDetail:str = obj["whereClauseTaxSvcDetail"]
      self.whereClauseTaxSvcJurDtl:str = obj["whereClauseTaxSvcJurDtl"]
      self.whereClauseTaxSvcMessages:str = obj["whereClauseTaxSvcMessages"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxReconciliationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaxHistoryByDateRange_input:
   """ Required : 
   startDate
   endDate
   """  
   def __init__(self, obj):
      self.startDate:str = obj["startDate"]
      """  Start Date to filter Avalara records.  """  
      self.endDate:str = obj["endDate"]
      """  End Date to filter Avalara records.  """  
      pass

class GetTaxHistoryByDateRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.resultCode:str = obj["parameters"]
      self.resultMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTaxHistory_input:
   """ Required : 
   lastDocID
   """  
   def __init__(self, obj):
      self.lastDocID:int = obj["lastDocID"]
      """  Used to select TaxSvcHead records.  """  
      pass

class GetTaxHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.resultCode:str = obj["parameters"]
      self.resultMessage:str = obj["parameters"]
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

class OnChangeofAction_input:
   """ Required : 
   action
   taxSvcID
   docType
   ds
   """  
   def __init__(self, obj):
      self.action:str = obj["action"]
      """  Action  """  
      self.taxSvcID:str = obj["taxSvcID"]
      """  TaxSvcID from TaxSvcHead.  """  
      self.docType:int = obj["docType"]
      """  DocType from TaxSvcHead.  """  
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

class OnChangeofAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PerformReconciliation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.resultStatus:bool = obj["resultStatus"]
      self.resultMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxReconciliationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxReconciliationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxReconciliationTableset] = obj["ds"]
      pass

      """  output parameters  """  

