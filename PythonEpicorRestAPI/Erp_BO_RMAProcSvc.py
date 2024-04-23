import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RMAProcSvc
# Description: RMA Processing business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMAProcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMAProcs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs",headers=creds) as resp:
           return await resp.json()

async def post_RMAProcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMAProcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs_Company_RMANum(Company, RMANum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMAProc item
   Description: Calls GetByID to retrieve the RMAProc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMAProcs_Company_RMANum(Company, RMANum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMAProc for the service
   Description: Calls UpdateExt to update RMAProc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMAProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMAProcs_Company_RMANum(Company, RMANum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMAProc item
   Description: Call UpdateExt to delete RMAProc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMAProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs_Company_RMANum_RMADtls(Company, RMANum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RMADtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMADtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMADtls",headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs_Company_RMANum_RMADtls_Company_RMANum_RMALine(Company, RMANum, RMALine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADtl item
   Description: Calls GetByID to retrieve the RMADtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs_Company_RMANum_RMAHeadAttches(Company, RMANum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RMAHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMAHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMAHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_RMAProcs_Company_RMANum_RMAHeadAttches_Company_RMANum_DrawingSeq(Company, RMANum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMAHeadAttch item
   Description: Calls GetByID to retrieve the RMAHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMADtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls",headers=creds) as resp:
           return await resp.json()

async def post_RMADtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine(Company, RMANum, RMALine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADtl item
   Description: Calls GetByID to retrieve the RMADtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMADtls_Company_RMANum_RMALine(Company, RMANum, RMALine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMADtl for the service
   Description: Calls UpdateExt to update RMADtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMADtls_Company_RMANum_RMALine(Company, RMANum, RMALine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMADtl item
   Description: Call UpdateExt to delete RMADtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_InvcDtls(Company, RMANum, RMALine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InvcDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InvcDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/InvcDtls",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, RMANum, RMALine, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_RMARcpts(Company, RMANum, RMALine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RMARcpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMARcpts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMARcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMARcpts",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMARcpt item
   Description: Calls GetByID to retrieve the RMARcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMARcpt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_RMADtlAttches(Company, RMANum, RMALine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RMADtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMADtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMADtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_RMADtls_Company_RMANum_RMALine_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company, RMANum, RMALine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADtlAttch item
   Description: Calls GetByID to retrieve the RMADtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls",headers=creds) as resp:
           return await resp.json()

async def post_InvcDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InvcDtl for the service
   Description: Calls UpdateExt to update InvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InvcDtl item
   Description: Call UpdateExt to delete InvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMARcpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMARcpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMARcpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMARcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts",headers=creds) as resp:
           return await resp.json()

async def post_RMARcpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMARcpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMARcptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMARcpt item
   Description: Calls GetByID to retrieve the RMARcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMARcpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMARcpt for the service
   Description: Calls UpdateExt to update RMARcpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMARcpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMARcpt item
   Description: Call UpdateExt to delete RMARcpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMARcpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMADtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_RMADtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company, RMANum, RMALine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADtlAttch item
   Description: Calls GetByID to retrieve the RMADtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company, RMANum, RMALine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMADtlAttch for the service
   Description: Calls UpdateExt to update RMADtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company, RMANum, RMALine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMADtlAttch item
   Description: Call UpdateExt to delete RMADtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMAHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMAHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMAHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_RMAHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMAHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMAHeadAttches_Company_RMANum_DrawingSeq(Company, RMANum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMAHeadAttch item
   Description: Calls GetByID to retrieve the RMAHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMAHeadAttches_Company_RMANum_DrawingSeq(Company, RMANum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMAHeadAttch for the service
   Description: Calls UpdateExt to update RMAHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMAHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMAHeadAttches_Company_RMANum_DrawingSeq(Company, RMANum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMAHeadAttch item
   Description: Call UpdateExt to delete RMAHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMAHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNumberSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNumberSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNumberSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNumberSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches",headers=creds) as resp:
           return await resp.json()

async def post_SerialNumberSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNumberSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNumberSearches_ProcessToken(ProcessToken, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNumberSearch item
   Description: Calls GetByID to retrieve the SerialNumberSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNumberSearches_ProcessToken(ProcessToken, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNumberSearch for the service
   Description: Calls UpdateExt to update SerialNumberSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNumberSearches_ProcessToken(ProcessToken, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNumberSearch item
   Description: Call UpdateExt to delete SerialNumberSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRMAHead, whereClauseRMAHeadAttch, whereClauseRMADtl, whereClauseRMADtlAttch, whereClauseInvcDtl, whereClauseRMARcpt, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSerialNumberSearch, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseRMAHead=" + whereClauseRMAHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMAHeadAttch=" + whereClauseRMAHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMADtl=" + whereClauseRMADtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMADtlAttch=" + whereClauseRMADtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInvcDtl=" + whereClauseInvcDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMARcpt=" + whereClauseRMARcpt
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
   params += "whereClauseSerialNumberSearch=" + whereClauseSerialNumberSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rmANum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "rmANum=" + rmANum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAttributeSetID
   Description: Call this method when the attribute set changes
   OperationID: ChangeAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeContact
   Description: Update RMA header contact information when the ConNum Contact is changed.
   OperationID: ChangeContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeContactRMADtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeContactRMADtl
   Description: Update RMA header contact information when the ConNum Contact is changed.
   OperationID: ChangeContactRMADtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContactRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContactRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomer
   Description: This populates the customer information in the RMAHead datatable.
   OperationID: ChangeCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderLine
   Description: This method validates the order line and updates the RMADtl record with values
from the line.
   OperationID: ChangeOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderNumber
   Description: This method validates that the order number entered exists and the customer on
the order matches the customer on the RMAHead record.
   OperationID: ChangeOrderNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderRelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderRelNum
   Description: This method validates the order release and updates the RMADtl record.
   OperationID: ChangeOrderRelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: This method validates the part number and updates the RMADtl record with values
from the part.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeReceivedQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeReceivedQty
   Description: This method validates the ReceivedQty and ReceivedQtyUOM
and updates the RMARcpt record.
   OperationID: ChangeReceivedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeReceivedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReceivedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevisionNum
   Description: Call this method when Revision changes to maintain inventory tracking
   OperationID: ChangeRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMADtlInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMADtlInvoiceLine
   Description: Update RMA Header InvoiceLine it is changed.
   OperationID: ChangeRMADtlInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMADtlInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMADtlInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMADtlLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMADtlLegalNumber
   Description: Update RMA Header LegalNumber it is changed.
   OperationID: ChangeRMADtlLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMADtlLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMADtlLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMAHeadLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMAHeadLegalNumber
   Description: Update RMA Header LegalNumber when it is changed.
   OperationID: ChangeRMAHeadLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMAHeadLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMAHeadLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipTo
   Description: This method validates the ShipToNum and updates the RMADtl record.
   OperationID: ChangeShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToCustID
   Description: This method validates the order release and updates the RMADtl record.
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouse
   Description: This method updates values in RMARcpt based on the new selling received quantity.
   OperationID: ChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCNCustomsDeclarationBillLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="bBeforeUpdate">if True - method is called before updating</param><param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSerialNumbers
   Description: This method returns text of a message to be asked if the number of serial numbers
selected does not match the quantity entered for the RMARcpt or RMADtl record.
The user has the option of continuing with the mismatch quantities or canceling.
This method should be called before the update method and should be called only when
part is serial number tracked and the quantity is greater than zero.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreditMemoExistsForRMA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreditMemoExistsForRMA
   Description: Checks if Credit memo exists for specified RMA
   OperationID: CreditMemoExistsForRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreditMemoExistsForRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreditMemoExistsForRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDateUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDateUser
   Description: This method puts a date/time/user stamp in the Note box for the user
   OperationID: GetDateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NoteUserAndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NoteUserAndDate
   Description: Add date/user stamp to note.
   OperationID: NoteUserAndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NoteUserAndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NoteUserAndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRMAUseRefCosts(epicorHeaders = None):
   """  
   Summary: Invoke method GetRMAUseRefCosts
   Description: This method will return company parameter 'Use Referenced Invoice Costs'.
   OperationID: GetRMAUseRefCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMAUseRefCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for an RMADtl or RMARcpt record and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Get all the parameters needed for launching Select Serial Numbers
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RMACreditAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RMACreditAdd
   Description: This method creates an RMA Credit record from the RMA Number and Line passed in.
The RMA Credit is stored in the InvcHead and InvcDtl tables.  Once the invoice is
created, the user has the option of updating the header and invoice line information.
It is expected that the A/R Invoice business object will be called to handle
the update of the header and/or line.
   OperationID: RMACreditAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RMACreditAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RMACreditAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRMANum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRMANum
   Description: Method to call when entering proposed RMA Number.  This method will return
two output variables.  One is a logical field to indicate if the RMA number
entered is existing or not.  The other variable is for the error message
in case the proposed RMA number is invalid.
   OperationID: CheckRMANum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_BuildttSelectedSerialNumbersForHelpDeskRMA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildttSelectedSerialNumbersForHelpDeskRMA
   Description: Validates that a single serial number passed serial number is valid for an RMADtl line
   OperationID: BuildttSelectedSerialNumbersForHelpDeskRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildttSelectedSerialNumbersForHelpDeskRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildttSelectedSerialNumbersForHelpDeskRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableIfPrinted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableIfPrinted
   Description: Logic if RMA is editable when RMA is printed
   OperationID: DisableIfPrinted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableIfPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableIfPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMAHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMAHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMAHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMAHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMAHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMAHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMAHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMAHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMAHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMAHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMADtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMADtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMADtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMADtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMADtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMARcpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMARcpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMARcpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMARcpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMARcpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMADtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMADtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMAHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMAHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMAHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMARcptRow] = obj["value"]
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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNumberSearchRow] = obj["value"]
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
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

class Erp_Tablesets_RMADtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RMANum:int = obj["RMANum"]
      self.RMALine:int = obj["RMALine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECC RMA Comment  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Num  """  
      self.ECCRMALine:int = obj["ECCRMALine"]
      """  ECC RMA Line  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  """  
      self.ConsolidateOneRelease:bool = obj["ConsolidateOneRelease"]
      """  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableAddCreditMemo:bool = obj["EnableAddCreditMemo"]
      """  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LocalizationFlag:str = obj["LocalizationFlag"]
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  The customer ID.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.AttrValueSetDescription:str = obj["AttrValueSetDescription"]
      self.AttrValueSetShortDescription:str = obj["AttrValueSetShortDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RMANum:int = obj["RMANum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadListRow:
   def __init__(self, obj):
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.RMADate:str = obj["RMADate"]
      """  Date of the Return Material Authorization.  Default as System date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  Reference to a customers accounts payable debit memo.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this RMA.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadRow:
   def __init__(self, obj):
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.RMADate:str = obj["RMADate"]
      """  Date of the Return Material Authorization.  Default as System date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  Reference to a customers accounts payable debit memo.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this RMA.  """  
      self.XRefRMANumber:str = obj["XRefRMANumber"]
      """  Cross reference RMA number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this RMA.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Ship To info is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RetInvoiceNum:str = obj["RetInvoiceNum"]
      """  The Return Invoice Number for the RMA (CSF - Turkey)  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Number  """  
      self.ECCCustRef:str = obj["ECCCustRef"]
      """  Customer Web Reference to RMA.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  DocumentPrinted  """  
      self.RMAComment:str = obj["RMAComment"]
      """  Comments about the RMA overall  """  
      self.WebComment:str = obj["WebComment"]
      """  Web Comments about the RMA overall  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      """  Bil to customer name  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerFSA:bool = obj["CustomerFSA"]
      """  Column to indicate if the customer set for the RMA is sync'd to FSA.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.FromFSA:bool = obj["FromFSA"]
      """  Column to indicate if the RMA was created on FSA.  """  
      self.WebAddressList:str = obj["WebAddressList"]
      """  Web address list for the contact who initiated the RMA.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMARcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.OpenReceipt:bool = obj["OpenReceipt"]
      """  This is set to NO when the entire quantity has been accounted for in RMADisp.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.DisposedQty:int = obj["DisposedQty"]
      """  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  """  
      self.CostUOM:str = obj["CostUOM"]
      """  Unit of measure that qualifies the unit costs.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the RMA line  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      self.EnableBin:bool = obj["EnableBin"]
      self.CustomerName:str = obj["CustomerName"]
      self.PartRevisionNum:str = obj["PartRevisionNum"]
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartPartDescription  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.ThisRcptQty:int = obj["ThisRcptQty"]
      """  The receipt quantity displayed in the RMADtl.ReturnQty.  """  
      self.ThisRcptQtyUOM:str = obj["ThisRcptQtyUOM"]
      """  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  """  
      self.DisposedQtyUOM:str = obj["DisposedQtyUOM"]
      """  Same value as ReceivedQtyUOM.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      self.IsPartMaster:bool = obj["IsPartMaster"]
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number used only for FSA  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
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

class Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.ProcessToken:str = obj["ProcessToken"]
      """  Token reserved for the process ID  """  
      self.GenericToken1:str = obj["GenericToken1"]
      """  1st generic token.  """  
      self.GenericToken2:str = obj["GenericToken2"]
      """  2nd generic token  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Returns where clause based on input tokens.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildttSelectedSerialNumbersForHelpDeskRMA_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class BuildttSelectedSerialNumbersForHelpDeskRMA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.snErrorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAttributeSetID_input:
   """ Required : 
   ds
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class ChangeAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeContactRMADtl_input:
   """ Required : 
   ds
   iConNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iConNum:int = obj["iConNum"]
      """  The proposed contact number  """  
      pass

class ChangeContactRMADtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeContact_input:
   """ Required : 
   ds
   iConNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iConNum:int = obj["iConNum"]
      """  The proposed contact number  """  
      pass

class ChangeContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomer_input:
   """ Required : 
   ds
   cCustID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cCustID:str = obj["cCustID"]
      """  The proposed customer id  """  
      pass

class ChangeCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderLine_input:
   """ Required : 
   ds
   iOrderLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iOrderLine:int = obj["iOrderLine"]
      """  The proposed order line  """  
      pass

class ChangeOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderNumber_input:
   """ Required : 
   ds
   iOrderNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iOrderNum:int = obj["iOrderNum"]
      """  The proposed order number  """  
      pass

class ChangeOrderNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderRelNum_input:
   """ Required : 
   ds
   iOrderRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iOrderRelNum:int = obj["iOrderRelNum"]
      """  The proposed order release number  """  
      pass

class ChangeOrderRelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   ds
   cPartNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cPartNum:str = obj["cPartNum"]
      """  The proposed part number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cPartNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeRMADtlInvoiceLine_input:
   """ Required : 
   ds
   ipInvoiceLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.ipInvoiceLine:int = obj["ipInvoiceLine"]
      """  The proposed InvoiceNum  """  
      pass

class ChangeRMADtlInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMADtlLegalNumber_input:
   """ Required : 
   ds
   ipLegalNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.ipLegalNumber:str = obj["ipLegalNumber"]
      """  The proposed LegalNumber  """  
      pass

class ChangeRMADtlLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMAHeadLegalNumber_input:
   """ Required : 
   ds
   ipLegalNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.ipLegalNumber:str = obj["ipLegalNumber"]
      """  The proposed LegalNumber  """  
      pass

class ChangeRMAHeadLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeReceivedQty_input:
   """ Required : 
   ds
   iReceivedQty
   iReceivedQtyUOM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iReceivedQty:int = obj["iReceivedQty"]
      """  The proposed received quantity  """  
      self.iReceivedQtyUOM:str = obj["iReceivedQtyUOM"]
      """  The proposed received quantity UOM  """  
      pass

class ChangeReceivedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRevisionNum_input:
   """ Required : 
   ds
   revisionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.revisionNum:str = obj["revisionNum"]
      """  The new Revision number  """  
      pass

class ChangeRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToCustID_input:
   """ Required : 
   ds
   ipShipToCustID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipToCustID.  """  
      pass

class ChangeShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipTo_input:
   """ Required : 
   ds
   iShipTo
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.iShipTo:str = obj["iShipTo"]
      """  The proposed ship to number  """  
      pass

class ChangeShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarehouse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class ChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCNCustomsDeclarationBillLine_input:
   """ Required : 
   bBeforeUpdate
   ds
   """  
   def __init__(self, obj):
      self.bBeforeUpdate:bool = obj["bBeforeUpdate"]
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class CheckCNCustomsDeclarationBillLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRMANum_input:
   """ Required : 
   proposedRMANum
   """  
   def __init__(self, obj):
      self.proposedRMANum:int = obj["proposedRMANum"]
      """  The proposed RMA Number  """  
      pass

class CheckRMANum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFoundRMA:bool = obj["opFoundRMA"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSerialNumbers_input:
   """ Required : 
   ds
   cTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cTableName:str = obj["cTableName"]
      """  The table name to check against; values are 'RMADtl' or 'RMARcpt'  """  
      pass

class CheckSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreditMemoExistsForRMA_input:
   """ Required : 
   rmaNum
   """  
   def __init__(self, obj):
      self.rmaNum:int = obj["rmaNum"]
      """  Number of RMA to check.  """  
      pass

class CreditMemoExistsForRMA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.rmaExists:bool = obj["rmaExists"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rmANum
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisableIfPrinted_input:
   """ Required : 
   tranDocTypeID
   ramPrinted
   """  
   def __init__(self, obj):
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      self.ramPrinted:bool = obj["ramPrinted"]
      pass

class DisableIfPrinted_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
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

class Erp_Tablesets_RMADtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RMANum:int = obj["RMANum"]
      self.RMALine:int = obj["RMALine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECC RMA Comment  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Num  """  
      self.ECCRMALine:int = obj["ECCRMALine"]
      """  ECC RMA Line  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  """  
      self.ConsolidateOneRelease:bool = obj["ConsolidateOneRelease"]
      """  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableAddCreditMemo:bool = obj["EnableAddCreditMemo"]
      """  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LocalizationFlag:str = obj["LocalizationFlag"]
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  The customer ID.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.AttrValueSetDescription:str = obj["AttrValueSetDescription"]
      self.AttrValueSetShortDescription:str = obj["AttrValueSetShortDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RMANum:int = obj["RMANum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadListRow:
   def __init__(self, obj):
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.RMADate:str = obj["RMADate"]
      """  Date of the Return Material Authorization.  Default as System date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  Reference to a customers accounts payable debit memo.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this RMA.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAHeadListTableset:
   def __init__(self, obj):
      self.RMAHeadList:list[Erp_Tablesets_RMAHeadListRow] = obj["RMAHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RMAHeadRow:
   def __init__(self, obj):
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.RMADate:str = obj["RMADate"]
      """  Date of the Return Material Authorization.  Default as System date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  Reference to a customers accounts payable debit memo.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this RMA.  """  
      self.XRefRMANumber:str = obj["XRefRMANumber"]
      """  Cross reference RMA number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this RMA.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Ship To info is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RetInvoiceNum:str = obj["RetInvoiceNum"]
      """  The Return Invoice Number for the RMA (CSF - Turkey)  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Number  """  
      self.ECCCustRef:str = obj["ECCCustRef"]
      """  Customer Web Reference to RMA.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  DocumentPrinted  """  
      self.RMAComment:str = obj["RMAComment"]
      """  Comments about the RMA overall  """  
      self.WebComment:str = obj["WebComment"]
      """  Web Comments about the RMA overall  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      """  Bil to customer name  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerFSA:bool = obj["CustomerFSA"]
      """  Column to indicate if the customer set for the RMA is sync'd to FSA.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.FromFSA:bool = obj["FromFSA"]
      """  Column to indicate if the RMA was created on FSA.  """  
      self.WebAddressList:str = obj["WebAddressList"]
      """  Web address list for the contact who initiated the RMA.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMAProcTableset:
   def __init__(self, obj):
      self.RMAHead:list[Erp_Tablesets_RMAHeadRow] = obj["RMAHead"]
      self.RMAHeadAttch:list[Erp_Tablesets_RMAHeadAttchRow] = obj["RMAHeadAttch"]
      self.RMADtl:list[Erp_Tablesets_RMADtlRow] = obj["RMADtl"]
      self.RMADtlAttch:list[Erp_Tablesets_RMADtlAttchRow] = obj["RMADtlAttch"]
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.RMARcpt:list[Erp_Tablesets_RMARcptRow] = obj["RMARcpt"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SerialNumberSearch:list[Erp_Tablesets_SerialNumberSearchRow] = obj["SerialNumberSearch"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RMARcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.OpenReceipt:bool = obj["OpenReceipt"]
      """  This is set to NO when the entire quantity has been accounted for in RMADisp.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.DisposedQty:int = obj["DisposedQty"]
      """  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  """  
      self.CostUOM:str = obj["CostUOM"]
      """  Unit of measure that qualifies the unit costs.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the RMA line  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      self.EnableBin:bool = obj["EnableBin"]
      self.CustomerName:str = obj["CustomerName"]
      self.PartRevisionNum:str = obj["PartRevisionNum"]
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartPartDescription  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.ThisRcptQty:int = obj["ThisRcptQty"]
      """  The receipt quantity displayed in the RMADtl.ReturnQty.  """  
      self.ThisRcptQtyUOM:str = obj["ThisRcptQtyUOM"]
      """  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  """  
      self.DisposedQtyUOM:str = obj["DisposedQtyUOM"]
      """  Same value as ReceivedQtyUOM.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      self.IsPartMaster:bool = obj["IsPartMaster"]
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number used only for FSA  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
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

class Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.ProcessToken:str = obj["ProcessToken"]
      """  Token reserved for the process ID  """  
      self.GenericToken1:str = obj["GenericToken1"]
      """  1st generic token.  """  
      self.GenericToken2:str = obj["GenericToken2"]
      """  2nd generic token  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Returns where clause based on input tokens.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtRMAProcTableset:
   def __init__(self, obj):
      self.RMAHead:list[Erp_Tablesets_RMAHeadRow] = obj["RMAHead"]
      self.RMAHeadAttch:list[Erp_Tablesets_RMAHeadAttchRow] = obj["RMAHeadAttch"]
      self.RMADtl:list[Erp_Tablesets_RMADtlRow] = obj["RMADtl"]
      self.RMADtlAttch:list[Erp_Tablesets_RMADtlAttchRow] = obj["RMADtlAttch"]
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.RMARcpt:list[Erp_Tablesets_RMARcptRow] = obj["RMARcpt"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SerialNumberSearch:list[Erp_Tablesets_SerialNumberSearchRow] = obj["SerialNumberSearch"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   rmANum
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMAProcTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RMAProcTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RMAProcTableset] = obj["returnObj"]
      pass

class GetDateUser_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class GetDateUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_RMAHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcDtl_input:
   """ Required : 
   ds
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewInvcDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMADtlAttch_input:
   """ Required : 
   ds
   rmANum
   rmALine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      pass

class GetNewRMADtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMADtl_input:
   """ Required : 
   ds
   rmANum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      pass

class GetNewRMADtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMAHeadAttch_input:
   """ Required : 
   ds
   rmANum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      pass

class GetNewRMAHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMAHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class GetNewRMAHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMARcpt_input:
   """ Required : 
   ds
   rmANum
   rmALine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      pass

class GetNewRMARcpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRMAUseRefCosts_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Company parameter 'Use Referenced Invoice Costs' value.  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseRMAHead
   whereClauseRMAHeadAttch
   whereClauseRMADtl
   whereClauseRMADtlAttch
   whereClauseInvcDtl
   whereClauseRMARcpt
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMAHead:str = obj["whereClauseRMAHead"]
      self.whereClauseRMAHeadAttch:str = obj["whereClauseRMAHeadAttch"]
      self.whereClauseRMADtl:str = obj["whereClauseRMADtl"]
      self.whereClauseRMADtlAttch:str = obj["whereClauseRMADtlAttch"]
      self.whereClauseInvcDtl:str = obj["whereClauseInvcDtl"]
      self.whereClauseRMARcpt:str = obj["whereClauseRMARcpt"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMAProcTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   ipTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.ipTableName:str = obj["ipTableName"]
      """  Table Name RMADtl or RMARcpt  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   cTableName
   iRMANum
   iRMALine
   iRMAReceipt
   ds
   """  
   def __init__(self, obj):
      self.cTableName:str = obj["cTableName"]
      """  The table to retrieve the serial numbers for. Valid values are:
            RMADtl or RMARcpt  """  
      self.iRMANum:int = obj["iRMANum"]
      """  The RMA Number  """  
      self.iRMALine:int = obj["iRMALine"]
      """  The RMA Detail line number  """  
      self.iRMAReceipt:int = obj["iRMAReceipt"]
      """  The RMA Receipt number; will be 0 when cTableName = RMADtl  """  
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
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

class NoteUserAndDate_input:
   """ Required : 
   currentNote
   """  
   def __init__(self, obj):
      self.currentNote:str = obj["currentNote"]
      pass

class NoteUserAndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.updatedNote:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class RMACreditAdd_input:
   """ Required : 
   iRMANum
   iRMALine
   iCorrection
   ds
   """  
   def __init__(self, obj):
      self.iRMANum:int = obj["iRMANum"]
      """  The RMA Number to create the invoice from  """  
      self.iRMALine:int = obj["iRMALine"]
      """  The RMA Line to create the invoice line from  """  
      self.iCorrection:bool = obj["iCorrection"]
      """  True will create a correction invoice, false will create a credit memo  """  
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class RMACreditAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iInvoiceNum:int = obj["parameters"]
      self.iInvoiceLine:int = obj["parameters"]
      self.opErrMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMAProcTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMAProcTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   ipTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      self.ipTableName:str = obj["ipTableName"]
      """  RMA TableName  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMAProcTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

