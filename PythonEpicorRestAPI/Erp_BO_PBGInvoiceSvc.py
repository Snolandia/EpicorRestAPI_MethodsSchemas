import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PBGInvoiceSvc
# Description: The PBGInvoice BO.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBGInvoices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvoices
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices",headers=creds) as resp:
           return await resp.json()

async def post_PBGInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum(Company, ProjectID, InvoiceNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvoice item
   Description: Calls GetByID to retrieve the PBGInvoice item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvoice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBGInvoices_Company_ProjectID_InvoiceNum(Company, ProjectID, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBGInvoice for the service
   Description: Calls UpdateExt to update PBGInvoice. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvoice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBGInvoices_Company_ProjectID_InvoiceNum(Company, ProjectID, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBGInvoice item
   Description: Call UpdateExt to delete PBGInvoice item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvoice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcBdns(Company, ProjectID, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PBGInvcBdns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcBdns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcBdnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcBdns",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company, ProjectID, InvoiceNum, RecSeq, BdnSetID, BdnCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcBdn item
   Description: Calls GetByID to retrieve the PBGInvcBdn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcBdn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RecSeq: Desc: RecSeq   Required: True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlFFs(Company, ProjectID, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PBGInvcDtlFFs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcDtlFFs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlFFRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlFFs",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcDtlFF item
   Description: Calls GetByID to retrieve the PBGInvcDtlFF item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlFF1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlTCs(Company, ProjectID, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PBGInvcDtlTCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcDtlTCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlTCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlTCs",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcDtlTC item
   Description: Calls GetByID to retrieve the PBGInvcDtlTC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlTC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBInvoicedAmts(Company, ProjectID, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PBInvoicedAmts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBInvoicedAmts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBInvoicedAmtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBInvoicedAmts",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvoices_Company_ProjectID_InvoiceNum_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company, ProjectID, InvoiceNum, RelatedToFile, TranKey, TaxCatID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBInvoicedAmt item
   Description: Calls GetByID to retrieve the PBInvoicedAmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBInvoicedAmt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param TranKey: Desc: TranKey   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcBdns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBGInvcBdns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcBdns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcBdnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns",headers=creds) as resp:
           return await resp.json()

async def post_PBGInvcBdns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcBdns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company, ProjectID, InvoiceNum, RecSeq, BdnSetID, BdnCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcBdn item
   Description: Calls GetByID to retrieve the PBGInvcBdn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcBdn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RecSeq: Desc: RecSeq   Required: True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company, ProjectID, InvoiceNum, RecSeq, BdnSetID, BdnCd, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBGInvcBdn for the service
   Description: Calls UpdateExt to update PBGInvcBdn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcBdn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RecSeq: Desc: RecSeq   Required: True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company, ProjectID, InvoiceNum, RecSeq, BdnSetID, BdnCd, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBGInvcBdn item
   Description: Call UpdateExt to delete PBGInvcBdn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcBdn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RecSeq: Desc: RecSeq   Required: True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcDtlFFs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBGInvcDtlFFs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcDtlFFs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlFFRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs",headers=creds) as resp:
           return await resp.json()

async def post_PBGInvcDtlFFs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcDtlFFs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcDtlFF item
   Description: Calls GetByID to retrieve the PBGInvcDtlFF item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlFF
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBGInvcDtlFF for the service
   Description: Calls UpdateExt to update PBGInvcDtlFF. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcDtlFF
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBGInvcDtlFF item
   Description: Call UpdateExt to delete PBGInvcDtlFF item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcDtlFF
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcDtlTCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBGInvcDtlTCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcDtlTCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlTCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs",headers=creds) as resp:
           return await resp.json()

async def post_PBGInvcDtlTCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcDtlTCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBGInvcDtlTC item
   Description: Calls GetByID to retrieve the PBGInvcDtlTC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlTC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBGInvcDtlTC for the service
   Description: Calls UpdateExt to update PBGInvcDtlTC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcDtlTC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company, ProjectID, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBGInvcDtlTC item
   Description: Call UpdateExt to delete PBGInvcDtlTC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcDtlTC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBInvoicedAmts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBInvoicedAmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBInvoicedAmts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBInvoicedAmtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts",headers=creds) as resp:
           return await resp.json()

async def post_PBInvoicedAmts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBInvoicedAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company, ProjectID, InvoiceNum, RelatedToFile, TranKey, TaxCatID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBInvoicedAmt item
   Description: Calls GetByID to retrieve the PBInvoicedAmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBInvoicedAmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param TranKey: Desc: TranKey   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company, ProjectID, InvoiceNum, RelatedToFile, TranKey, TaxCatID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBInvoicedAmt for the service
   Description: Calls UpdateExt to update PBInvoicedAmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBInvoicedAmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param TranKey: Desc: TranKey   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company, ProjectID, InvoiceNum, RelatedToFile, TranKey, TaxCatID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBInvoicedAmt item
   Description: Call UpdateExt to delete PBInvoicedAmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBInvoicedAmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param TranKey: Desc: TranKey   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBPrjInvcPhaseLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBPrjInvcPhaseLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBPrjInvcPhaseLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBPrjInvcPhaseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists",headers=creds) as resp:
           return await resp.json()

async def post_PBPrjInvcPhaseLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBPrjInvcPhaseLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBPrjInvcPhaseLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBPrjInvcPhaseList item
   Description: Calls GetByID to retrieve the PBPrjInvcPhaseList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBPrjInvcPhaseList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBPrjInvcPhaseLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBPrjInvcPhaseList for the service
   Description: Calls UpdateExt to update PBPrjInvcPhaseList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBPrjInvcPhaseList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBPrjInvcPhaseLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBPrjInvcPhaseList item
   Description: Call UpdateExt to delete PBPrjInvcPhaseList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBPrjInvcPhaseList
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PBProjectsLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PBProjectsLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBProjectsLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBProjectsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists",headers=creds) as resp:
           return await resp.json()

async def post_PBProjectsLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBProjectsLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PBProjectsLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PBProjectsList item
   Description: Calls GetByID to retrieve the PBProjectsList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBProjectsList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PBProjectsLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PBProjectsList for the service
   Description: Calls UpdateExt to update PBProjectsList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBProjectsList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PBProjectsLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PBProjectsList item
   Description: Call UpdateExt to delete PBProjectsList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBProjectsList
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePBGInvcHead, whereClausePBGInvcBdn, whereClausePBGInvcDtlFF, whereClausePBGInvcDtlTC, whereClausePBInvoicedAmt, whereClausePBPrjInvcPhaseList, whereClausePBProjectsList, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePBGInvcHead=" + whereClausePBGInvcHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBGInvcBdn=" + whereClausePBGInvcBdn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBGInvcDtlFF=" + whereClausePBGInvcDtlFF
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBGInvcDtlTC=" + whereClausePBGInvcDtlTC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBInvoicedAmt=" + whereClausePBInvoicedAmt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBPrjInvcPhaseList=" + whereClausePBPrjInvcPhaseList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePBProjectsList=" + whereClausePBProjectsList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(projectID, invoiceNum, epicorHeaders = None):
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
   params += "projectID=" + projectID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveInvoice
   Description: ApproveInvoice.
   OperationID: ApproveInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataByProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataByProjectID
   Description: Custom GetRows method to retrieve data by ProjectID and ConInvMeth.
   OperationID: GetDataByProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataByProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataByProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataByTempInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataByTempInvoiceNum
   Description: Get temp invoice num to call GetByID procedure.
   OperationID: GetDataByTempInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataByTempInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataByTempInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPBGInvcHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPBGInvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPBGInvcBdn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPBGInvcBdn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcBdn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcBdn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcBdn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPBGInvcDtlFF(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPBGInvcDtlFF
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcDtlFF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcDtlFF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcDtlFF_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPBGInvcDtlTC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPBGInvcDtlTC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcDtlTC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcDtlTC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcDtlTC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPBInvoicedAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPBInvoicedAmt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBInvoicedAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBInvoicedAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBInvoicedAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBGInvcBdnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBGInvcDtlFFRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBGInvcDtlTCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBGInvcHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBGInvcHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBInvoicedAmtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBPrjInvcPhaseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBPrjInvcPhaseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBProjectsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PBProjectsListRow] = obj["value"]
      pass

class Erp_Tablesets_PBGInvcBdnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set Id  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code  """  
      self.BdnPrc:int = obj["BdnPrc"]
      """  Burden Percentage  """  
      self.BdnLbrAmt:int = obj["BdnLbrAmt"]
      """  Burden Labor Amount  """  
      self.BdnConLbrAmt:int = obj["BdnConLbrAmt"]
      """  Burden Labor Contract Amount  """  
      self.BdnSubAmt:int = obj["BdnSubAmt"]
      """  Burden subcontract amount  """  
      self.BdnMtlAmt:int = obj["BdnMtlAmt"]
      """  Burden Material Amount  """  
      self.BdnMiscAmt:int = obj["BdnMiscAmt"]
      """  Burden Other Direct Cost Amount  """  
      self.RecSeq:int = obj["RecSeq"]
      """   Sequence,
zero for original Invoice when InvoiceNum = 0 , 
next for the recalculations. 
-1 = true up process for whole project  """  
      self.RecDate:str = obj["RecDate"]
      """  Date of the recalculations  """  
      self.DocBdnLbrAmt:int = obj["DocBdnLbrAmt"]
      """  Burden Labor Amount in the Project currency  """  
      self.Rpt1BdnLbrAmt:int = obj["Rpt1BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.Rpt2BdnLbrAmt:int = obj["Rpt2BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.Rpt3BdnLbrAmt:int = obj["Rpt3BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.DocBdnConLbrAmt:int = obj["DocBdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Project currency  """  
      self.Rpt1BdnConLbrAmt:int = obj["Rpt1BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.Rpt2BdnConLbrAmt:int = obj["Rpt2BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.Rpt3BdnConLbrAmt:int = obj["Rpt3BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.DocBdnSubAmt:int = obj["DocBdnSubAmt"]
      """  Burden subcontract amount in the Project currency  """  
      self.Rpt1BdnSubAmt:int = obj["Rpt1BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.Rpt2BdnSubAmt:int = obj["Rpt2BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.Rpt3BdnSubAmt:int = obj["Rpt3BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.DocBdnMtlAmt:int = obj["DocBdnMtlAmt"]
      """  Burden Material Amount in the Project currency  """  
      self.Rpt1BdnMtlAmt:int = obj["Rpt1BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.Rpt2BdnMtlAmt:int = obj["Rpt2BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.Rpt3BdnMtlAmt:int = obj["Rpt3BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.DocBdnMiscAmt:int = obj["DocBdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Project currency  """  
      self.Rpt1BdnMiscAmt:int = obj["Rpt1BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.Rpt2BdnMiscAmt:int = obj["Rpt2BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.Rpt3BdnMiscAmt:int = obj["Rpt3BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.DocActTotalAmt:int = obj["DocActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user.  """  
      self.DocInvTotalAmt:int = obj["DocInvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency  """  
      self.ActTotalAmt:int = obj["ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Base currency  """  
      self.Rpt1ActTotalAmt:int = obj["Rpt1ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.Rpt2ActTotalAmt:int = obj["Rpt2ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.Rpt3ActTotalAmt:int = obj["Rpt3ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.InvTotalAmt:int = obj["InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Project currency  """  
      self.Rpt1InvTotalAmt:int = obj["Rpt1InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.Rpt2InvTotalAmt:int = obj["Rpt2InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.Rpt3InvTotalAmt:int = obj["Rpt3InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.BdnRuleAmt:int = obj["BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  """  
      self.DocBdnRuleAmt:int = obj["DocBdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Project currency  """  
      self.Rpt1BdnRuleAmt:int = obj["Rpt1BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.Rpt2BdnRuleAmt:int = obj["Rpt2BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.Rpt3BdnRuleAmt:int = obj["Rpt3BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.BdnCdDescription:str = obj["BdnCdDescription"]
      self.BdnSetIDDescription:str = obj["BdnSetIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcDtlFFRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Sequence  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  """  
      self.TranFile:str = obj["TranFile"]
      """  File where transaction was from  """  
      self.TranKey:str = obj["TranKey"]
      """  Key to the actual source document  """  
      self.BillSchedID:str = obj["BillSchedID"]
      """  Billing Schedule ID  """  
      self.Manager:str = obj["Manager"]
      """  Manager  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales Order Line  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code  """  
      self.RetentionPcnt:int = obj["RetentionPcnt"]
      """  Retention Percent  """  
      self.ReduceInvByRet:bool = obj["ReduceInvByRet"]
      """  Reduce Invoice By Retention  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Measured Work ID  """  
      self.DtlSeq:int = obj["DtlSeq"]
      """  Activity ID  """  
      self.ActivityUnit:str = obj["ActivityUnit"]
      """  P=Percentage, H=Hours, C=Cost, L=Linear, M=Monetary  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price Per Unit  """  
      self.ContractPrc:int = obj["ContractPrc"]
      """  Percentage of Contract  """  
      self.ParentWrkSchID:str = obj["ParentWrkSchID"]
      """  Parent Work Schedule ID  """  
      self.CustQtySurveyor:str = obj["CustQtySurveyor"]
      """  Customer Quantity Surveyor  """  
      self.ApprovalAmt:int = obj["ApprovalAmt"]
      """  Approval Amount  """  
      self.ApprovalDate:str = obj["ApprovalDate"]
      """  Approval Date  """  
      self.ActStatus:str = obj["ActStatus"]
      """  S = Progress, D = Dispute, A = Approved, P = Posted.  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.NettActivityAmt:int = obj["NettActivityAmt"]
      """  Net Activity Amount  """  
      self.ActivityAmount:int = obj["ActivityAmount"]
      """  Activity Amount  """  
      self.CostPlusPrc:int = obj["CostPlusPrc"]
      """  Cost Plus percentage  """  
      self.QtySurveyor:str = obj["QtySurveyor"]
      """  Quantity Surveyor from the Activity Detail  """  
      self.DocApprovalAmt:int = obj["DocApprovalAmt"]
      """  in the Project currency  """  
      self.Rpt1ApprovalAmt:int = obj["Rpt1ApprovalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2ApprovalAmt:int = obj["Rpt2ApprovalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3ApprovalAmt:int = obj["Rpt3ApprovalAmt"]
      """  in the Reporting currency  """  
      self.DocActivityAmount:int = obj["DocActivityAmount"]
      """  in the Project currency  """  
      self.Rpt1ActivityAmount:int = obj["Rpt1ActivityAmount"]
      """  in the Reporting currency  """  
      self.Rpt2ActivityAmount:int = obj["Rpt2ActivityAmount"]
      """  in the Reporting currency  """  
      self.Rpt3ActivityAmount:int = obj["Rpt3ActivityAmount"]
      """  in the Reporting currency  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  in the Reporting currency  """  
      self.DocNettActivityAmt:int = obj["DocNettActivityAmt"]
      """  in the Project currency  """  
      self.Rpt1NettActivityAmt:int = obj["Rpt1NettActivityAmt"]
      """  in the Reporting currency  """  
      self.Rpt2NettActivityAmt:int = obj["Rpt2NettActivityAmt"]
      """  in the Reporting currency  """  
      self.Rpt3NettActivityAmt:int = obj["Rpt3NettActivityAmt"]
      """  in the Reporting currency  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price Per Unit in Document currency  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Price Per Unit in Report Currency 1  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Price Per Unit in Report Currency 2  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Price Per Unit in Report Currency 3  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.MarkUpAmt:int = obj["MarkUpAmt"]
      self.DocMarkUpAmt:int = obj["DocMarkUpAmt"]
      self.Rpt1MarkUpAmt:int = obj["Rpt1MarkUpAmt"]
      self.Rpt2MarkUpAmt:int = obj["Rpt2MarkUpAmt"]
      self.Rpt3MarkUpAmt:int = obj["Rpt3MarkUpAmt"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      """  Phase Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PBillSchDescription:str = obj["PBillSchDescription"]
      self.PBSchWrkDescription:str = obj["PBSchWrkDescription"]
      self.PBWrkMeasuredDtlDescription:str = obj["PBWrkMeasuredDtlDescription"]
      self.PBWrkMeasuredHeadDescription:str = obj["PBWrkMeasuredHeadDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcDtlTCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Sequence  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  """  
      self.TranFile:str = obj["TranFile"]
      """  File where transaction was from  """  
      self.TranKey:str = obj["TranKey"]
      """  Key to the actual source document  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence of the Job that the labor transaction applies to  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.MatNum:int = obj["MatNum"]
      """  Material Sequence  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  Employee Number  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.LbrRateFrom:str = obj["LbrRateFrom"]
      """   List of the values:PROJ = Project, EMPL = Employee,
ROLE = Role, LBR = Labor Details  """  
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge Rate  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order Number  """  
      self.POLine:int = obj["POLine"]
      """  Purchase Order Line  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing Slip Line  """  
      self.SubExtAmt:int = obj["SubExtAmt"]
      """  Subcontract Amount  """  
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      """  subcontract mark up percent  """  
      self.SubMarkUpAmt:int = obj["SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  """  
      self.SubTotalAmt:int = obj["SubTotalAmt"]
      """  Total Subcontract Amount  """  
      self.Hours:int = obj["Hours"]
      """  Hours  """  
      self.LbrExtAmt:int = obj["LbrExtAmt"]
      """  Labor Amount  """  
      self.PBLbrMarkUp:int = obj["PBLbrMarkUp"]
      """  Labor Cost Markup percent  """  
      self.LbrMarkUpAmt:int = obj["LbrMarkUpAmt"]
      """  Labor Cost Amount  """  
      self.LbrTotalAmt:int = obj["LbrTotalAmt"]
      """  Total Labor Amount  """  
      self.MtlCost:int = obj["MtlCost"]
      """  Material Cost  """  
      self.MtlExtAmt:int = obj["MtlExtAmt"]
      """  Material  Amount  """  
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      """  Material mark up percent  """  
      self.MtlMarkUpAmt:int = obj["MtlMarkUpAmt"]
      """  Material Cost Amount  """  
      self.MtlTotalAmt:int = obj["MtlTotalAmt"]
      """  Total Material Amount  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Total Ceiling  """  
      self.PBCeilingFee:int = obj["PBCeilingFee"]
      """  Fee Ceiling  """  
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      """  Other Cost Ceiling  """  
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      """  Burden Ceiling  """  
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      """  Material Burden Ceiling  """  
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      """  Material Ceiling  """  
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      """  Subcontract Ceiling  """  
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      """  Labor Ceiling  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Individual Ceilings on Suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Individual Ceilings on Employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Individual Ceilings on Project Role  """  
      self.OverCeilingPrj:int = obj["OverCeilingPrj"]
      """  Project Over Ceiling  """  
      self.OverCeilingFee:int = obj["OverCeilingFee"]
      """  Fee Over Ceiling  """  
      self.OverCeilingBur:int = obj["OverCeilingBur"]
      """  Burden Over Ceiling  """  
      self.OverCeilingMisc:int = obj["OverCeilingMisc"]
      """  Other Cost Over Ceiling  """  
      self.OverCeilingSub:int = obj["OverCeilingSub"]
      """  Subcontract Over Ceiling  """  
      self.OverCeilingMtlBur:int = obj["OverCeilingMtlBur"]
      """  Material Burden Over Ceiling  """  
      self.OverCeilingMtl:int = obj["OverCeilingMtl"]
      """  Material Over Ceiling  """  
      self.OverCeilingLbr:int = obj["OverCeilingLbr"]
      """  Labor Over Ceiling  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      """  Retention Percentage  """  
      self.ContrLbr:bool = obj["ContrLbr"]
      """  Contract Labor  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity  """  
      self.PriceFrom:str = obj["PriceFrom"]
      """   Following options: PRJ = Project Price List,
CUS = Customer Price List, GEN = General Price List, TRN = Transaction  """  
      self.PartTranType:str = obj["PartTranType"]
      """  Transaction Type  """  
      self.CutLineAmt:int = obj["CutLineAmt"]
      """  Reduced Line amount  """  
      self.OverCeilingAmt:int = obj["OverCeilingAmt"]
      """  Over Ceiling  """  
      self.CeilingAmt:int = obj["CeilingAmt"]
      """  Ceiling  """  
      self.CeilingFrom:str = obj["CeilingFrom"]
      """  Ceiling comes From: RoleCd, Employee, Supplier  """  
      self.CurrentInvoicedAmt:int = obj["CurrentInvoicedAmt"]
      """  Current Invoice Amount  """  
      self.MiscExtAmt:int = obj["MiscExtAmt"]
      """  ODC Amount  """  
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      """  ODC markup percent. If Invoicing Type = CP then Copy of Project.PBMiscMarkUp  """  
      self.MiscMarkUpAmt:int = obj["MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100  """  
      self.MiscTotalAmt:int = obj["MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Misc Change ID for TM/CP Invoices  """  
      self.LbrInvAmt:int = obj["LbrInvAmt"]
      """  Labor Invoiced Amount  """  
      self.MtlInvAmt:int = obj["MtlInvAmt"]
      """  Material Invoiced Amount  """  
      self.SubInvAmt:int = obj["SubInvAmt"]
      """  Subcontract Invoiced Amount  """  
      self.BdnInvAmt:int = obj["BdnInvAmt"]
      """  Burden Invoiced Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and APInvoiceNum make up the unique key to the APInvDtl table.  """  
      self.SubLbrAmt:int = obj["SubLbrAmt"]
      """  Subcontract labor  """  
      self.SubMtlAmt:int = obj["SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts)  """  
      self.DocLbrExtAmt:int = obj["DocLbrExtAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrExtAmt:int = obj["Rpt1LbrExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrExtAmt:int = obj["Rpt2LbrExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrExtAmt:int = obj["Rpt3LbrExtAmt"]
      """  in the Reporting currency  """  
      self.DocLbrMarkUpAmt:int = obj["DocLbrMarkUpAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrMarkUpAmt:int = obj["Rpt1LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrMarkUpAmt:int = obj["Rpt2LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrMarkUpAmt:int = obj["Rpt3LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.DocLbrTotalAmt:int = obj["DocLbrTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrTotalAmt:int = obj["Rpt1LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrTotalAmt:int = obj["Rpt2LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrTotalAmt:int = obj["Rpt3LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.DocMtlExtAmt:int = obj["DocMtlExtAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlExtAmt:int = obj["Rpt1MtlExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlExtAmt:int = obj["Rpt2MtlExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlExtAmt:int = obj["Rpt3MtlExtAmt"]
      """  in the Reporting currency  """  
      self.DocMtlMarkUpAmt:int = obj["DocMtlMarkUpAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlMarkUpAmt:int = obj["Rpt1MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlMarkUpAmt:int = obj["Rpt2MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlMarkUpAmt:int = obj["Rpt3MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.DocMtlTotalAmt:int = obj["DocMtlTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlTotalAmt:int = obj["Rpt1MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlTotalAmt:int = obj["Rpt2MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlTotalAmt:int = obj["Rpt3MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.DocSubExtAmt:int = obj["DocSubExtAmt"]
      """  in the Project currency  """  
      self.Rpt1SubExtAmt:int = obj["Rpt1SubExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubExtAmt:int = obj["Rpt2SubExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubExtAmt:int = obj["Rpt3SubExtAmt"]
      """  in the Reporting currency  """  
      self.DocSubMarkUpAmt:int = obj["DocSubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Project currency  """  
      self.Rpt1SubMarkUpAmt:int = obj["Rpt1SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.Rpt2SubMarkUpAmt:int = obj["Rpt2SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.Rpt3SubMarkUpAmt:int = obj["Rpt3SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.DocSubTotalAmt:int = obj["DocSubTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1SubTotalAmt:int = obj["Rpt1SubTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubTotalAmt:int = obj["Rpt2SubTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubTotalAmt:int = obj["Rpt3SubTotalAmt"]
      """  in the Reporting currency  """  
      self.DocMiscExtAmt:int = obj["DocMiscExtAmt"]
      """  ODC Amount in the Project currency  """  
      self.Rpt1MiscExtAmt:int = obj["Rpt1MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.Rpt2MiscExtAmt:int = obj["Rpt2MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.Rpt3MiscExtAmt:int = obj["Rpt3MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.DocMiscMarkUpAmt:int = obj["DocMiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Project currency  """  
      self.Rpt1MiscMarkUpAmt:int = obj["Rpt1MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.Rpt2MiscMarkUpAmt:int = obj["Rpt2MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.Rpt3MiscMarkUpAmt:int = obj["Rpt3MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.DocMiscTotalAmt:int = obj["DocMiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Project currency  """  
      self.Rpt1MiscTotalAmt:int = obj["Rpt1MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.Rpt2MiscTotalAmt:int = obj["Rpt2MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.Rpt3MiscTotalAmt:int = obj["Rpt3MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.DocMtlCost:int = obj["DocMtlCost"]
      """  in the Project currency  """  
      self.Rpt1MtlCost:int = obj["Rpt1MtlCost"]
      """  in the Reporting currency  """  
      self.Rpt2MtlCost:int = obj["Rpt2MtlCost"]
      """  in the Reporting currency  """  
      self.Rpt3MtlCost:int = obj["Rpt3MtlCost"]
      """  in the Reporting currency  """  
      self.DocCutLineAmt:int = obj["DocCutLineAmt"]
      """  Reduced Line amount in the Project currency  """  
      self.Rpt1CutLineAmt:int = obj["Rpt1CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.Rpt2CutLineAmt:int = obj["Rpt2CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.Rpt3CutLineAmt:int = obj["Rpt3CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.DocCeilingAmt:int = obj["DocCeilingAmt"]
      """  Ceiling in the Project currency  """  
      self.Rpt1CeilingAmt:int = obj["Rpt1CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.Rpt2CeilingAmt:int = obj["Rpt2CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.Rpt3CeilingAmt:int = obj["Rpt3CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.DocOverCeilingAmt:int = obj["DocOverCeilingAmt"]
      """  Over Ceiling in the Project currency  """  
      self.Rpt1OverCeilingAmt:int = obj["Rpt1OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.Rpt2OverCeilingAmt:int = obj["Rpt2OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.Rpt3OverCeilingAmt:int = obj["Rpt3OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.DocCurrentInvoicedAmt:int = obj["DocCurrentInvoicedAmt"]
      """  in the Project currency  """  
      self.Rpt1CurrentInvoicedAmt:int = obj["Rpt1CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.Rpt2CurrentInvoicedAmt:int = obj["Rpt2CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.Rpt3CurrentInvoicedAmt:int = obj["Rpt3CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.DocLbrInvAmt:int = obj["DocLbrInvAmt"]
      """  Labor Invoiced Amount in the Project currency  """  
      self.Rpt1LbrInvAmt:int = obj["Rpt1LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.Rpt2LbrInvAmt:int = obj["Rpt2LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.Rpt3LbrInvAmt:int = obj["Rpt3LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.DocMtlInvAmt:int = obj["DocMtlInvAmt"]
      """  Material Invoiced Amount in the Project currency  """  
      self.Rpt1MtlInvAmt:int = obj["Rpt1MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.Rpt2MtlInvAmt:int = obj["Rpt2MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.Rpt3MtlInvAmt:int = obj["Rpt3MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.DocSubInvAmt:int = obj["DocSubInvAmt"]
      """  Subcontract Invoiced Amount in the Project currency  """  
      self.Rpt1SubInvAmt:int = obj["Rpt1SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.Rpt2SubInvAmt:int = obj["Rpt2SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.Rpt3SubInvAmt:int = obj["Rpt3SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.DocBdnInvAmt:int = obj["DocBdnInvAmt"]
      """  Burden Invoiced Amount in the Project currency  """  
      self.Rpt1BdnInvAmt:int = obj["Rpt1BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.Rpt2BdnInvAmt:int = obj["Rpt2BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.Rpt3BdnInvAmt:int = obj["Rpt3BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.DocSubLbrAmt:int = obj["DocSubLbrAmt"]
      """  Subcontract labor in the Project currency  """  
      self.Rpt1SubLbrAmt:int = obj["Rpt1SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.Rpt2SubLbrAmt:int = obj["Rpt2SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.Rpt3SubLbrAmt:int = obj["Rpt3SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.DocSubMtlAmt:int = obj["DocSubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Project currency  """  
      self.Rpt1SubMtlAmt:int = obj["Rpt1SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.Rpt2SubMtlAmt:int = obj["Rpt2SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.Rpt3SubMtlAmt:int = obj["Rpt3SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.PBRoleMarkup:int = obj["PBRoleMarkup"]
      """  Role Mark Up percentage  """  
      self.PackNum:str = obj["PackNum"]
      """  reference to Pack Slip number  """  
      self.DocChargeRate:int = obj["DocChargeRate"]
      """  Charge Rate  """  
      self.Rpt1ChargeRate:int = obj["Rpt1ChargeRate"]
      """  Charge Rate  """  
      self.Rpt2ChargeRate:int = obj["Rpt2ChargeRate"]
      """  Charge Rate  """  
      self.Rpt3ChargeRate:int = obj["Rpt3ChargeRate"]
      """  Charge Rate  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  in the Reporting currency  """  
      self.ToDelete:bool = obj["ToDelete"]
      """  Field to be deleted in Invoice Review, means that the related transaction will be skipped in the Recalculation of the Invoice  """  
      self.UpdatedAmt:bool = obj["UpdatedAmt"]
      """  Flag indicated that the amount has been updated in the Invoice Review program  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  copy from LaborDtl.TimeTypCd  """  
      self.ParentInvoiceLine:int = obj["ParentInvoiceLine"]
      """  Reference to the Parent Line from the Ceiling Line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.Comment:str = obj["Comment"]
      """  Line Comment  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  OrderRelNum  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  PriceListCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.DspCPMarkUpAmt:int = obj["DspCPMarkUpAmt"]
      self.DspCPMarkUpPrc:int = obj["DspCPMarkUpPrc"]
      self.DspCPTotalAmt:int = obj["DspCPTotalAmt"]
      self.DspLbrAssemblySeq:int = obj["DspLbrAssemblySeq"]
      self.DspLbrJobNum:str = obj["DspLbrJobNum"]
      self.DspLbrOprSeq:int = obj["DspLbrOprSeq"]
      self.DspMtlAssemblySeq:int = obj["DspMtlAssemblySeq"]
      self.DspMtlJobNum:str = obj["DspMtlJobNum"]
      self.DspMtlOprSeq:int = obj["DspMtlOprSeq"]
      self.DspSubAssemblySeq:int = obj["DspSubAssemblySeq"]
      self.DspSubJobNum:str = obj["DspSubJobNum"]
      self.DspSubOprSeq:int = obj["DspSubOprSeq"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      """  Phase Description  """  
      self.Rpt1TotLineAmt:int = obj["Rpt1TotLineAmt"]
      self.Rpt2TotLineAmt:int = obj["Rpt2TotLineAmt"]
      self.Rpt3TotLineAmt:str = obj["Rpt3TotLineAmt"]
      self.TotLineAmt:int = obj["TotLineAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocTotLineAmt:int = obj["DocTotLineAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  """  
      self.TmpInvcNum:int = obj["TmpInvcNum"]
      """  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  """  
      self.DspProjectInvcNum:str = obj["DspProjectInvcNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Actual Invoice date  """  
      self.DspInvoiceNum:int = obj["DspInvoiceNum"]
      self.DspTempInvcNum:int = obj["DspTempInvcNum"]
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.PrcStatus:str = obj["PrcStatus"]
      """  A = Approved, P = Posted, empty - review  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  """  
      self.TmpInvcNum:int = obj["TmpInvcNum"]
      """  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  """  
      self.ConReference:str = obj["ConReference"]
      """  Contract Reference  """  
      self.TmpInvcDate:str = obj["TmpInvcDate"]
      """  Date the user entered in Invoice Preparation form  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Actual Invoice date  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the Contract  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  """  
      self.PBFeePrjType:str = obj["PBFeePrjType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeePrjApply:str = obj["PBFeePrjApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeePrjCharge:int = obj["PBFeePrjCharge"]
      """  Project Fee Charge  """  
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      """  Subcontract Fee Charge  """  
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      """  Material Fee Charge  """  
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      """  Labor Fee Charge  """  
      self.BdnAmt:int = obj["BdnAmt"]
      """  Burden Amount  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  Other Direct Coat Amount  """  
      self.SubAmt:int = obj["SubAmt"]
      """  Subcontract Amount  """  
      self.MtlAmt:int = obj["MtlAmt"]
      """  Material Amount  """  
      self.LbrAmt:int = obj["LbrAmt"]
      """  Labor Amount  """  
      self.PBFeeTotal:int = obj["PBFeeTotal"]
      """  Total Fee  """  
      self.PBFeePrjAmt:int = obj["PBFeePrjAmt"]
      """  Project Fee Amount  """  
      self.PBFeeSubAmt:int = obj["PBFeeSubAmt"]
      """  Subcontract Fee Amount  """  
      self.PBFeeMtlAmt:int = obj["PBFeeMtlAmt"]
      """  Material Fee Amount  """  
      self.PBFeeLbrAmt:int = obj["PBFeeLbrAmt"]
      """  Labor Fee Amount  """  
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      """  N = Net Cost, G = Gross Cost  """  
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      """  The percentage to be retained, this can be 0.  """  
      self.RetentionProc:str = obj["RetentionProc"]
      """  Retention Processing with a system list of options: M - Maximum of Contract Value, I - Invoice Value  """  
      self.PBFeeRetentionAmt:int = obj["PBFeeRetentionAmt"]
      """  Fee Retention Amount  """  
      self.PBFeeNettAmt:int = obj["PBFeeNettAmt"]
      """  Fee Nett Amount  """  
      self.InvcTotalSumAmt:int = obj["InvcTotalSumAmt"]
      """  Summa of elements amounts  """  
      self.InvcAddFeeAmt:int = obj["InvcAddFeeAmt"]
      """  Total amount plus Fee  """  
      self.InvcCutCeiling:int = obj["InvcCutCeiling"]
      """  Total reduced by Ceiling  """  
      self.InvcCutRetention:int = obj["InvcCutRetention"]
      """  Total redused by Retention  """  
      self.InvcTotal:int = obj["InvcTotal"]
      """  Final Total Invoice  """  
      self.PrcStatus:str = obj["PrcStatus"]
      """  A = Approved, P = Posted, empty - review  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  Parameter of the Invoice Preparation process  """  
      self.PBCeilingFee:int = obj["PBCeilingFee"]
      """  Fee Ceiling  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Total Ceiling  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Individual Ceilings on Suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Individual Ceilings on Employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Individual Ceilings on Role  """  
      self.OverCeilingFees:int = obj["OverCeilingFees"]
      """  OverCeiling Fees (negative)  """  
      self.OverCeilingTotalAmt:int = obj["OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      """  Percentage of Progress Payment, for PP invoice only.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the invoice was approved for posting  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  Approved by user id  """  
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeLbrAmt:int = obj["DocPBFeeLbrAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeLbrAmt:int = obj["Rpt1PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeLbrAmt:int = obj["Rpt2PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeLbrAmt:int = obj["Rpt3PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeMtlAmt:int = obj["DocPBFeeMtlAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeMtlAmt:int = obj["Rpt1PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeMtlAmt:int = obj["Rpt2PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeMtlAmt:int = obj["Rpt3PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeSubAmt:int = obj["DocPBFeeSubAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeSubAmt:int = obj["Rpt1PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeSubAmt:int = obj["Rpt2PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeSubAmt:int = obj["Rpt3PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeePrjCharge:int = obj["DocPBFeePrjCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeePrjCharge:int = obj["Rpt1PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeePrjCharge:int = obj["Rpt2PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeePrjCharge:int = obj["Rpt3PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeTotal:int = obj["DocPBFeeTotal"]
      """  in the Project currency  """  
      self.Rpt1PBFeeTotal:int = obj["Rpt1PBFeeTotal"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeTotal:int = obj["Rpt2PBFeeTotal"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeTotal:int = obj["Rpt3PBFeeTotal"]
      """  in the Reporting currency  """  
      self.DocLbrAmt:int = obj["DocLbrAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrAmt:int = obj["Rpt1LbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrAmt:int = obj["Rpt2LbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrAmt:int = obj["Rpt3LbrAmt"]
      """  in the Reporting currency  """  
      self.DocMtlAmt:int = obj["DocMtlAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlAmt:int = obj["Rpt1MtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlAmt:int = obj["Rpt2MtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlAmt:int = obj["Rpt3MtlAmt"]
      """  in the Reporting currency  """  
      self.DocSubAmt:int = obj["DocSubAmt"]
      """  in the Project currency  """  
      self.Rpt1SubAmt:int = obj["Rpt1SubAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubAmt:int = obj["Rpt2SubAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubAmt:int = obj["Rpt3SubAmt"]
      """  in the Reporting currency  """  
      self.DocBdnAmt:int = obj["DocBdnAmt"]
      """  in the Project currency  """  
      self.Rpt1BdnAmt:int = obj["Rpt1BdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt2BdnAmt:int = obj["Rpt2BdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt3BdnAmt:int = obj["Rpt3BdnAmt"]
      """  in the Reporting currency  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  in the Project currency  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  in the Reporting currency  """  
      self.DocPBCeilingFee:int = obj["DocPBCeilingFee"]
      """  Fee Ceiling in the Project currency  """  
      self.Rpt1PBCeilingFee:int = obj["Rpt1PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.Rpt2PBCeilingFee:int = obj["Rpt2PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.Rpt3PBCeilingFee:int = obj["Rpt3PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      """  in the Project currency  """  
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.DocOverCeilingFees:int = obj["DocOverCeilingFees"]
      """  OverCeiling Fees (negative) in the Project currency  """  
      self.Rpt1OverCeilingFees:int = obj["Rpt1OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.Rpt2OverCeilingFees:int = obj["Rpt2OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.Rpt3OverCeilingFees:int = obj["Rpt3OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  Retention Amount in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.DocOverCeilingTotalAmt:int = obj["DocOverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Project currency  """  
      self.Rpt1OverCeilingTotalAmt:int = obj["Rpt1OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.Rpt2OverCeilingTotalAmt:int = obj["Rpt2OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.Rpt3OverCeilingTotalAmt:int = obj["Rpt3OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.DocPBFeeRetentionAmt:int = obj["DocPBFeeRetentionAmt"]
      """  Fee Retention Amount in the Project currency  """  
      self.Rpt1PBFeeRetentionAmt:int = obj["Rpt1PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.Rpt2PBFeeRetentionAmt:int = obj["Rpt2PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.Rpt3PBFeeRetentionAmt:int = obj["Rpt3PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.DocPBFeeNettAmt:int = obj["DocPBFeeNettAmt"]
      """  Fee Nett Amount in the Project currency  """  
      self.Rpt1PBFeeNettAmt:int = obj["Rpt1PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.Rpt2PBFeeNettAmt:int = obj["Rpt2PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.Rpt3PBFeeNettAmt:int = obj["Rpt3PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.DocInvcTotalSumAmt:int = obj["DocInvcTotalSumAmt"]
      """  Summa of elements amounts  in the Project currency  """  
      self.Rpt1InvcTotalSumAmt:int = obj["Rpt1InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.Rpt2InvcTotalSumAmt:int = obj["Rpt2InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.Rpt3InvcTotalSumAmt:int = obj["Rpt3InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.DocInvcAddFeeAmt:int = obj["DocInvcAddFeeAmt"]
      """  Total amount plus Fee in the Project currency  """  
      self.Rpt1InvcAddFeeAmt:int = obj["Rpt1InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.Rpt2InvcAddFeeAmt:int = obj["Rpt2InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.Rpt3InvcAddFeeAmt:int = obj["Rpt3InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.DocInvcCutCeiling:int = obj["DocInvcCutCeiling"]
      """  Total reduced by Ceiling in the Project currency  """  
      self.Rpt1InvcCutCeiling:int = obj["Rpt1InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.Rpt2InvcCutCeiling:int = obj["Rpt2InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.Rpt3InvcCutCeiling:int = obj["Rpt3InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.DocInvcTotal:int = obj["DocInvcTotal"]
      """  Final Total Invoice in the Project currency  """  
      self.Rpt1InvcTotal:int = obj["Rpt1InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.Rpt2InvcTotal:int = obj["Rpt2InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.Rpt3InvcTotal:int = obj["Rpt3InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.SumLbrTotalAmt:int = obj["SumLbrTotalAmt"]
      """  Labor actual amount  """  
      self.SumMtlTotalAmt:int = obj["SumMtlTotalAmt"]
      """  Material actual amount  """  
      self.SumSubTotalAmt:int = obj["SumSubTotalAmt"]
      """  Subcontract actual amount  """  
      self.SumBdnAmt:int = obj["SumBdnAmt"]
      """  Burden actual amount  """  
      self.DocSumLbrTotalAmt:int = obj["DocSumLbrTotalAmt"]
      """  Labor actual amount in the Project currency  """  
      self.Rpt1SumLbrTotalAmt:int = obj["Rpt1SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.Rpt2SumLbrTotalAmt:int = obj["Rpt2SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.Rpt3SumLbrTotalAmt:int = obj["Rpt3SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.DocSumMtlTotalAmt:int = obj["DocSumMtlTotalAmt"]
      """  Material actual amount in the Project currency  """  
      self.Rpt1SumMtlTotalAmt:int = obj["Rpt1SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.Rpt2SumMtlTotalAmt:int = obj["Rpt2SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.Rpt3SumMtlTotalAmt:int = obj["Rpt3SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.DocSumSubTotalAmt:int = obj["DocSumSubTotalAmt"]
      """  Subcontract actual amount in the Project currency  """  
      self.Rpt1SumSubTotalAmt:int = obj["Rpt1SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.Rpt2SumSubTotalAmt:int = obj["Rpt2SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.Rpt3SumSubTotalAmt:int = obj["Rpt3SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.DocSumBdnAmt:int = obj["DocSumBdnAmt"]
      """  in the Project currency  """  
      self.Rpt1SumBdnAmt:int = obj["Rpt1SumBdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SumBdnAmt:int = obj["Rpt2SumBdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SumBdnAmt:int = obj["Rpt3SumBdnAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeePrjAmt:int = obj["DocPBFeePrjAmt"]
      """  Project Fee Amount in Document Currency  """  
      self.Rpt1PBFeePrjAmt:int = obj["Rpt1PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 1  """  
      self.Rpt2PBFeePrjAmt:int = obj["Rpt2PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 2  """  
      self.Rpt3PBFeePrjAmt:int = obj["Rpt3PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 3  """  
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      """   Other Direct Cost Fee Type
List of options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      """   Other Direct Cost Fee Apply Type
List of options: F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied  """  
      self.PBFeeMiscAmt:int = obj["PBFeeMiscAmt"]
      """  Calculated ODC Fee amount  """  
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Project currency  """  
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.DocPBFeeMiscAmt:int = obj["DocPBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Project currency  """  
      self.Rpt1PBFeeMiscAmt:int = obj["Rpt1PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.Rpt2PBFeeMiscAmt:int = obj["Rpt2PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.Rpt3PBFeeMiscAmt:int = obj["Rpt3PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      """  Retention percentage. How this is used is dependent on RetentionProc field.  """  
      self.Updated:bool = obj["Updated"]
      """  Flag indicated that one of its lines has been updated or deleted in the Invoice Review program  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Indicates if invoice should be auto printed  """  
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      """  Fee Invoice Text  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.PPAllOrderLines:bool = obj["PPAllOrderLines"]
      """  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  """  
      self.PPAllPrjJobs:bool = obj["PPAllPrjJobs"]
      """  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      """  Flag indicates if AR invoices are allowed to be generated even if the element is over the predefined ceiling (limit), also indicates if the invoice amount should stay limited or not when ceiling exists. It is copied from the current value of Project flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  Base Currency ID  """  
      self.DspInvoiceNum:int = obj["DspInvoiceNum"]
      self.DspTempInvcNum:int = obj["DspTempInvcNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.ProjectIDConReference:str = obj["ProjectIDConReference"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBInvoicedAmtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  Related To File  """  
      self.TranKey:str = obj["TranKey"]
      """  Transaction Key  """  
      self.DocPrepAmt:int = obj["DocPrepAmt"]
      """  Amount strored by Invoice Preparation before Posting ,used to appropriate compare with Ceiling  """  
      self.PrepOverCeiling:int = obj["PrepOverCeiling"]
      """  Preparation over ceiling in Base curency  """  
      self.DocPrepOverCeiling:int = obj["DocPrepOverCeiling"]
      """  Preparation over ceiling in Document curency  """  
      self.GenOverCeiling:int = obj["GenOverCeiling"]
      """  Generated Over ceiling in Base currency  """  
      self.DocGenOverCeiling:int = obj["DocGenOverCeiling"]
      """  Generated Over ceiling in Document currency  """  
      self.PostOverCeiling:int = obj["PostOverCeiling"]
      """  Posted Over Ceiling in Base currency  """  
      self.DocPostOverCeiling:int = obj["DocPostOverCeiling"]
      """  Posted Over Ceiling in Document currency  """  
      self.GenAmt:int = obj["GenAmt"]
      """  Ceiling Generated Consumed in Base currency  """  
      self.DocGenAmt:int = obj["DocGenAmt"]
      """  Ceiling Generated Consumed in Document currency  """  
      self.PostAmt:int = obj["PostAmt"]
      """  Ceiling Posted Consumed in Base currency  """  
      self.DocPostAmt:int = obj["DocPostAmt"]
      """  Ceiling Posted Consumed in Document currency  """  
      self.PrepAmt:int = obj["PrepAmt"]
      """  Ceiling Preparation Consumed in Document currency  """  
      self.CeilingLimit:int = obj["CeilingLimit"]
      """  Ceiling Limit in Base currency  """  
      self.DocCeilingLimit:int = obj["DocCeilingLimit"]
      """  Ceiling Limit in Project Currency  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice Number. It's zero for preparation and total values for whole project  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBPrjInvcPhaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ProjectID:str = obj["ProjectID"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.PhaseID:str = obj["PhaseID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBProjectsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ProjectID:str = obj["ProjectID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveInvoice_input:
   """ Required : 
   ipProjectID
   askWarning
   ds
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The ProjectID.  """  
      self.askWarning:bool = obj["askWarning"]
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

class ApproveInvoice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   projectID
   invoiceNum
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PBGInvcBdnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set Id  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code  """  
      self.BdnPrc:int = obj["BdnPrc"]
      """  Burden Percentage  """  
      self.BdnLbrAmt:int = obj["BdnLbrAmt"]
      """  Burden Labor Amount  """  
      self.BdnConLbrAmt:int = obj["BdnConLbrAmt"]
      """  Burden Labor Contract Amount  """  
      self.BdnSubAmt:int = obj["BdnSubAmt"]
      """  Burden subcontract amount  """  
      self.BdnMtlAmt:int = obj["BdnMtlAmt"]
      """  Burden Material Amount  """  
      self.BdnMiscAmt:int = obj["BdnMiscAmt"]
      """  Burden Other Direct Cost Amount  """  
      self.RecSeq:int = obj["RecSeq"]
      """   Sequence,
zero for original Invoice when InvoiceNum = 0 , 
next for the recalculations. 
-1 = true up process for whole project  """  
      self.RecDate:str = obj["RecDate"]
      """  Date of the recalculations  """  
      self.DocBdnLbrAmt:int = obj["DocBdnLbrAmt"]
      """  Burden Labor Amount in the Project currency  """  
      self.Rpt1BdnLbrAmt:int = obj["Rpt1BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.Rpt2BdnLbrAmt:int = obj["Rpt2BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.Rpt3BdnLbrAmt:int = obj["Rpt3BdnLbrAmt"]
      """  Burden Labor Amount in the Reporting currency  """  
      self.DocBdnConLbrAmt:int = obj["DocBdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Project currency  """  
      self.Rpt1BdnConLbrAmt:int = obj["Rpt1BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.Rpt2BdnConLbrAmt:int = obj["Rpt2BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.Rpt3BdnConLbrAmt:int = obj["Rpt3BdnConLbrAmt"]
      """  Burden Labor Contract Amount in the Reporting currency  """  
      self.DocBdnSubAmt:int = obj["DocBdnSubAmt"]
      """  Burden subcontract amount in the Project currency  """  
      self.Rpt1BdnSubAmt:int = obj["Rpt1BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.Rpt2BdnSubAmt:int = obj["Rpt2BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.Rpt3BdnSubAmt:int = obj["Rpt3BdnSubAmt"]
      """  Burden subcontract amount in the Reporting currency  """  
      self.DocBdnMtlAmt:int = obj["DocBdnMtlAmt"]
      """  Burden Material Amount in the Project currency  """  
      self.Rpt1BdnMtlAmt:int = obj["Rpt1BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.Rpt2BdnMtlAmt:int = obj["Rpt2BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.Rpt3BdnMtlAmt:int = obj["Rpt3BdnMtlAmt"]
      """  Burden Material Amount in the Reporting currency  """  
      self.DocBdnMiscAmt:int = obj["DocBdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Project currency  """  
      self.Rpt1BdnMiscAmt:int = obj["Rpt1BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.Rpt2BdnMiscAmt:int = obj["Rpt2BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.Rpt3BdnMiscAmt:int = obj["Rpt3BdnMiscAmt"]
      """  Burden Other Direct Cost Amount in the Reporting currency  """  
      self.DocActTotalAmt:int = obj["DocActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user.  """  
      self.DocInvTotalAmt:int = obj["DocInvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency  """  
      self.ActTotalAmt:int = obj["ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Base currency  """  
      self.Rpt1ActTotalAmt:int = obj["Rpt1ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.Rpt2ActTotalAmt:int = obj["Rpt2ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.Rpt3ActTotalAmt:int = obj["Rpt3ActTotalAmt"]
      """  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  """  
      self.InvTotalAmt:int = obj["InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Project currency  """  
      self.Rpt1InvTotalAmt:int = obj["Rpt1InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.Rpt2InvTotalAmt:int = obj["Rpt2InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.Rpt3InvTotalAmt:int = obj["Rpt3InvTotalAmt"]
      """  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  """  
      self.BdnRuleAmt:int = obj["BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  """  
      self.DocBdnRuleAmt:int = obj["DocBdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Project currency  """  
      self.Rpt1BdnRuleAmt:int = obj["Rpt1BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.Rpt2BdnRuleAmt:int = obj["Rpt2BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.Rpt3BdnRuleAmt:int = obj["Rpt3BdnRuleAmt"]
      """  Burden calculated from other burdens according to the rules  in the Reporting currency  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.BdnCdDescription:str = obj["BdnCdDescription"]
      self.BdnSetIDDescription:str = obj["BdnSetIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcDtlFFRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Sequence  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  """  
      self.TranFile:str = obj["TranFile"]
      """  File where transaction was from  """  
      self.TranKey:str = obj["TranKey"]
      """  Key to the actual source document  """  
      self.BillSchedID:str = obj["BillSchedID"]
      """  Billing Schedule ID  """  
      self.Manager:str = obj["Manager"]
      """  Manager  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales Order Line  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code  """  
      self.RetentionPcnt:int = obj["RetentionPcnt"]
      """  Retention Percent  """  
      self.ReduceInvByRet:bool = obj["ReduceInvByRet"]
      """  Reduce Invoice By Retention  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Measured Work ID  """  
      self.DtlSeq:int = obj["DtlSeq"]
      """  Activity ID  """  
      self.ActivityUnit:str = obj["ActivityUnit"]
      """  P=Percentage, H=Hours, C=Cost, L=Linear, M=Monetary  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price Per Unit  """  
      self.ContractPrc:int = obj["ContractPrc"]
      """  Percentage of Contract  """  
      self.ParentWrkSchID:str = obj["ParentWrkSchID"]
      """  Parent Work Schedule ID  """  
      self.CustQtySurveyor:str = obj["CustQtySurveyor"]
      """  Customer Quantity Surveyor  """  
      self.ApprovalAmt:int = obj["ApprovalAmt"]
      """  Approval Amount  """  
      self.ApprovalDate:str = obj["ApprovalDate"]
      """  Approval Date  """  
      self.ActStatus:str = obj["ActStatus"]
      """  S = Progress, D = Dispute, A = Approved, P = Posted.  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.NettActivityAmt:int = obj["NettActivityAmt"]
      """  Net Activity Amount  """  
      self.ActivityAmount:int = obj["ActivityAmount"]
      """  Activity Amount  """  
      self.CostPlusPrc:int = obj["CostPlusPrc"]
      """  Cost Plus percentage  """  
      self.QtySurveyor:str = obj["QtySurveyor"]
      """  Quantity Surveyor from the Activity Detail  """  
      self.DocApprovalAmt:int = obj["DocApprovalAmt"]
      """  in the Project currency  """  
      self.Rpt1ApprovalAmt:int = obj["Rpt1ApprovalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2ApprovalAmt:int = obj["Rpt2ApprovalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3ApprovalAmt:int = obj["Rpt3ApprovalAmt"]
      """  in the Reporting currency  """  
      self.DocActivityAmount:int = obj["DocActivityAmount"]
      """  in the Project currency  """  
      self.Rpt1ActivityAmount:int = obj["Rpt1ActivityAmount"]
      """  in the Reporting currency  """  
      self.Rpt2ActivityAmount:int = obj["Rpt2ActivityAmount"]
      """  in the Reporting currency  """  
      self.Rpt3ActivityAmount:int = obj["Rpt3ActivityAmount"]
      """  in the Reporting currency  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  in the Reporting currency  """  
      self.DocNettActivityAmt:int = obj["DocNettActivityAmt"]
      """  in the Project currency  """  
      self.Rpt1NettActivityAmt:int = obj["Rpt1NettActivityAmt"]
      """  in the Reporting currency  """  
      self.Rpt2NettActivityAmt:int = obj["Rpt2NettActivityAmt"]
      """  in the Reporting currency  """  
      self.Rpt3NettActivityAmt:int = obj["Rpt3NettActivityAmt"]
      """  in the Reporting currency  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price Per Unit in Document currency  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Price Per Unit in Report Currency 1  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Price Per Unit in Report Currency 2  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Price Per Unit in Report Currency 3  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.MarkUpAmt:int = obj["MarkUpAmt"]
      self.DocMarkUpAmt:int = obj["DocMarkUpAmt"]
      self.Rpt1MarkUpAmt:int = obj["Rpt1MarkUpAmt"]
      self.Rpt2MarkUpAmt:int = obj["Rpt2MarkUpAmt"]
      self.Rpt3MarkUpAmt:int = obj["Rpt3MarkUpAmt"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      """  Phase Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PBillSchDescription:str = obj["PBillSchDescription"]
      self.PBSchWrkDescription:str = obj["PBSchWrkDescription"]
      self.PBWrkMeasuredDtlDescription:str = obj["PBWrkMeasuredDtlDescription"]
      self.PBWrkMeasuredHeadDescription:str = obj["PBWrkMeasuredHeadDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcDtlTCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Sequence  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  """  
      self.TranFile:str = obj["TranFile"]
      """  File where transaction was from  """  
      self.TranKey:str = obj["TranKey"]
      """  Key to the actual source document  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence of the Job that the labor transaction applies to  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.MatNum:int = obj["MatNum"]
      """  Material Sequence  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  Employee Number  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.LbrRateFrom:str = obj["LbrRateFrom"]
      """   List of the values:PROJ = Project, EMPL = Employee,
ROLE = Role, LBR = Labor Details  """  
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge Rate  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order Number  """  
      self.POLine:int = obj["POLine"]
      """  Purchase Order Line  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing Slip Line  """  
      self.SubExtAmt:int = obj["SubExtAmt"]
      """  Subcontract Amount  """  
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      """  subcontract mark up percent  """  
      self.SubMarkUpAmt:int = obj["SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  """  
      self.SubTotalAmt:int = obj["SubTotalAmt"]
      """  Total Subcontract Amount  """  
      self.Hours:int = obj["Hours"]
      """  Hours  """  
      self.LbrExtAmt:int = obj["LbrExtAmt"]
      """  Labor Amount  """  
      self.PBLbrMarkUp:int = obj["PBLbrMarkUp"]
      """  Labor Cost Markup percent  """  
      self.LbrMarkUpAmt:int = obj["LbrMarkUpAmt"]
      """  Labor Cost Amount  """  
      self.LbrTotalAmt:int = obj["LbrTotalAmt"]
      """  Total Labor Amount  """  
      self.MtlCost:int = obj["MtlCost"]
      """  Material Cost  """  
      self.MtlExtAmt:int = obj["MtlExtAmt"]
      """  Material  Amount  """  
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      """  Material mark up percent  """  
      self.MtlMarkUpAmt:int = obj["MtlMarkUpAmt"]
      """  Material Cost Amount  """  
      self.MtlTotalAmt:int = obj["MtlTotalAmt"]
      """  Total Material Amount  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Total Ceiling  """  
      self.PBCeilingFee:int = obj["PBCeilingFee"]
      """  Fee Ceiling  """  
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      """  Other Cost Ceiling  """  
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      """  Burden Ceiling  """  
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      """  Material Burden Ceiling  """  
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      """  Material Ceiling  """  
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      """  Subcontract Ceiling  """  
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      """  Labor Ceiling  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Individual Ceilings on Suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Individual Ceilings on Employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Individual Ceilings on Project Role  """  
      self.OverCeilingPrj:int = obj["OverCeilingPrj"]
      """  Project Over Ceiling  """  
      self.OverCeilingFee:int = obj["OverCeilingFee"]
      """  Fee Over Ceiling  """  
      self.OverCeilingBur:int = obj["OverCeilingBur"]
      """  Burden Over Ceiling  """  
      self.OverCeilingMisc:int = obj["OverCeilingMisc"]
      """  Other Cost Over Ceiling  """  
      self.OverCeilingSub:int = obj["OverCeilingSub"]
      """  Subcontract Over Ceiling  """  
      self.OverCeilingMtlBur:int = obj["OverCeilingMtlBur"]
      """  Material Burden Over Ceiling  """  
      self.OverCeilingMtl:int = obj["OverCeilingMtl"]
      """  Material Over Ceiling  """  
      self.OverCeilingLbr:int = obj["OverCeilingLbr"]
      """  Labor Over Ceiling  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      """  Retention Percentage  """  
      self.ContrLbr:bool = obj["ContrLbr"]
      """  Contract Labor  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity  """  
      self.PriceFrom:str = obj["PriceFrom"]
      """   Following options: PRJ = Project Price List,
CUS = Customer Price List, GEN = General Price List, TRN = Transaction  """  
      self.PartTranType:str = obj["PartTranType"]
      """  Transaction Type  """  
      self.CutLineAmt:int = obj["CutLineAmt"]
      """  Reduced Line amount  """  
      self.OverCeilingAmt:int = obj["OverCeilingAmt"]
      """  Over Ceiling  """  
      self.CeilingAmt:int = obj["CeilingAmt"]
      """  Ceiling  """  
      self.CeilingFrom:str = obj["CeilingFrom"]
      """  Ceiling comes From: RoleCd, Employee, Supplier  """  
      self.CurrentInvoicedAmt:int = obj["CurrentInvoicedAmt"]
      """  Current Invoice Amount  """  
      self.MiscExtAmt:int = obj["MiscExtAmt"]
      """  ODC Amount  """  
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      """  ODC markup percent. If Invoicing Type = CP then Copy of Project.PBMiscMarkUp  """  
      self.MiscMarkUpAmt:int = obj["MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100  """  
      self.MiscTotalAmt:int = obj["MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Misc Change ID for TM/CP Invoices  """  
      self.LbrInvAmt:int = obj["LbrInvAmt"]
      """  Labor Invoiced Amount  """  
      self.MtlInvAmt:int = obj["MtlInvAmt"]
      """  Material Invoiced Amount  """  
      self.SubInvAmt:int = obj["SubInvAmt"]
      """  Subcontract Invoiced Amount  """  
      self.BdnInvAmt:int = obj["BdnInvAmt"]
      """  Burden Invoiced Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and APInvoiceNum make up the unique key to the APInvDtl table.  """  
      self.SubLbrAmt:int = obj["SubLbrAmt"]
      """  Subcontract labor  """  
      self.SubMtlAmt:int = obj["SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts)  """  
      self.DocLbrExtAmt:int = obj["DocLbrExtAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrExtAmt:int = obj["Rpt1LbrExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrExtAmt:int = obj["Rpt2LbrExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrExtAmt:int = obj["Rpt3LbrExtAmt"]
      """  in the Reporting currency  """  
      self.DocLbrMarkUpAmt:int = obj["DocLbrMarkUpAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrMarkUpAmt:int = obj["Rpt1LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrMarkUpAmt:int = obj["Rpt2LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrMarkUpAmt:int = obj["Rpt3LbrMarkUpAmt"]
      """  in the Reporting currency  """  
      self.DocLbrTotalAmt:int = obj["DocLbrTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrTotalAmt:int = obj["Rpt1LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrTotalAmt:int = obj["Rpt2LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrTotalAmt:int = obj["Rpt3LbrTotalAmt"]
      """  in the Reporting currency  """  
      self.DocMtlExtAmt:int = obj["DocMtlExtAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlExtAmt:int = obj["Rpt1MtlExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlExtAmt:int = obj["Rpt2MtlExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlExtAmt:int = obj["Rpt3MtlExtAmt"]
      """  in the Reporting currency  """  
      self.DocMtlMarkUpAmt:int = obj["DocMtlMarkUpAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlMarkUpAmt:int = obj["Rpt1MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlMarkUpAmt:int = obj["Rpt2MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlMarkUpAmt:int = obj["Rpt3MtlMarkUpAmt"]
      """  in the Reporting currency  """  
      self.DocMtlTotalAmt:int = obj["DocMtlTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlTotalAmt:int = obj["Rpt1MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlTotalAmt:int = obj["Rpt2MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlTotalAmt:int = obj["Rpt3MtlTotalAmt"]
      """  in the Reporting currency  """  
      self.DocSubExtAmt:int = obj["DocSubExtAmt"]
      """  in the Project currency  """  
      self.Rpt1SubExtAmt:int = obj["Rpt1SubExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubExtAmt:int = obj["Rpt2SubExtAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubExtAmt:int = obj["Rpt3SubExtAmt"]
      """  in the Reporting currency  """  
      self.DocSubMarkUpAmt:int = obj["DocSubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Project currency  """  
      self.Rpt1SubMarkUpAmt:int = obj["Rpt1SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.Rpt2SubMarkUpAmt:int = obj["Rpt2SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.Rpt3SubMarkUpAmt:int = obj["Rpt3SubMarkUpAmt"]
      """  Subcontract Cost Markup Amount  in the Reporting currency  """  
      self.DocSubTotalAmt:int = obj["DocSubTotalAmt"]
      """  in the Project currency  """  
      self.Rpt1SubTotalAmt:int = obj["Rpt1SubTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubTotalAmt:int = obj["Rpt2SubTotalAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubTotalAmt:int = obj["Rpt3SubTotalAmt"]
      """  in the Reporting currency  """  
      self.DocMiscExtAmt:int = obj["DocMiscExtAmt"]
      """  ODC Amount in the Project currency  """  
      self.Rpt1MiscExtAmt:int = obj["Rpt1MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.Rpt2MiscExtAmt:int = obj["Rpt2MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.Rpt3MiscExtAmt:int = obj["Rpt3MiscExtAmt"]
      """  ODC Amount in the Reporting currency  """  
      self.DocMiscMarkUpAmt:int = obj["DocMiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Project currency  """  
      self.Rpt1MiscMarkUpAmt:int = obj["Rpt1MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.Rpt2MiscMarkUpAmt:int = obj["Rpt2MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.Rpt3MiscMarkUpAmt:int = obj["Rpt3MiscMarkUpAmt"]
      """  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  """  
      self.DocMiscTotalAmt:int = obj["DocMiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Project currency  """  
      self.Rpt1MiscTotalAmt:int = obj["Rpt1MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.Rpt2MiscTotalAmt:int = obj["Rpt2MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.Rpt3MiscTotalAmt:int = obj["Rpt3MiscTotalAmt"]
      """  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  """  
      self.DocMtlCost:int = obj["DocMtlCost"]
      """  in the Project currency  """  
      self.Rpt1MtlCost:int = obj["Rpt1MtlCost"]
      """  in the Reporting currency  """  
      self.Rpt2MtlCost:int = obj["Rpt2MtlCost"]
      """  in the Reporting currency  """  
      self.Rpt3MtlCost:int = obj["Rpt3MtlCost"]
      """  in the Reporting currency  """  
      self.DocCutLineAmt:int = obj["DocCutLineAmt"]
      """  Reduced Line amount in the Project currency  """  
      self.Rpt1CutLineAmt:int = obj["Rpt1CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.Rpt2CutLineAmt:int = obj["Rpt2CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.Rpt3CutLineAmt:int = obj["Rpt3CutLineAmt"]
      """  Reduced Line amount in the Reporting currency  """  
      self.DocCeilingAmt:int = obj["DocCeilingAmt"]
      """  Ceiling in the Project currency  """  
      self.Rpt1CeilingAmt:int = obj["Rpt1CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.Rpt2CeilingAmt:int = obj["Rpt2CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.Rpt3CeilingAmt:int = obj["Rpt3CeilingAmt"]
      """  Ceiling in the Reporting currency  """  
      self.DocOverCeilingAmt:int = obj["DocOverCeilingAmt"]
      """  Over Ceiling in the Project currency  """  
      self.Rpt1OverCeilingAmt:int = obj["Rpt1OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.Rpt2OverCeilingAmt:int = obj["Rpt2OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.Rpt3OverCeilingAmt:int = obj["Rpt3OverCeilingAmt"]
      """  Over Ceiling in the Reporting currency  """  
      self.DocCurrentInvoicedAmt:int = obj["DocCurrentInvoicedAmt"]
      """  in the Project currency  """  
      self.Rpt1CurrentInvoicedAmt:int = obj["Rpt1CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.Rpt2CurrentInvoicedAmt:int = obj["Rpt2CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.Rpt3CurrentInvoicedAmt:int = obj["Rpt3CurrentInvoicedAmt"]
      """  in the Reporting currency  """  
      self.DocLbrInvAmt:int = obj["DocLbrInvAmt"]
      """  Labor Invoiced Amount in the Project currency  """  
      self.Rpt1LbrInvAmt:int = obj["Rpt1LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.Rpt2LbrInvAmt:int = obj["Rpt2LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.Rpt3LbrInvAmt:int = obj["Rpt3LbrInvAmt"]
      """  Labor Invoiced Amount in the Reporting currency  """  
      self.DocMtlInvAmt:int = obj["DocMtlInvAmt"]
      """  Material Invoiced Amount in the Project currency  """  
      self.Rpt1MtlInvAmt:int = obj["Rpt1MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.Rpt2MtlInvAmt:int = obj["Rpt2MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.Rpt3MtlInvAmt:int = obj["Rpt3MtlInvAmt"]
      """  Material Invoiced Amount in the Reporting currency  """  
      self.DocSubInvAmt:int = obj["DocSubInvAmt"]
      """  Subcontract Invoiced Amount in the Project currency  """  
      self.Rpt1SubInvAmt:int = obj["Rpt1SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.Rpt2SubInvAmt:int = obj["Rpt2SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.Rpt3SubInvAmt:int = obj["Rpt3SubInvAmt"]
      """  Subcontract Invoiced Amount in the Reporting currency  """  
      self.DocBdnInvAmt:int = obj["DocBdnInvAmt"]
      """  Burden Invoiced Amount in the Project currency  """  
      self.Rpt1BdnInvAmt:int = obj["Rpt1BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.Rpt2BdnInvAmt:int = obj["Rpt2BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.Rpt3BdnInvAmt:int = obj["Rpt3BdnInvAmt"]
      """  Burden Invoiced Amount in the Reporting currency  """  
      self.DocSubLbrAmt:int = obj["DocSubLbrAmt"]
      """  Subcontract labor in the Project currency  """  
      self.Rpt1SubLbrAmt:int = obj["Rpt1SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.Rpt2SubLbrAmt:int = obj["Rpt2SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.Rpt3SubLbrAmt:int = obj["Rpt3SubLbrAmt"]
      """  Subcontract labor in the Reporting currency  """  
      self.DocSubMtlAmt:int = obj["DocSubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Project currency  """  
      self.Rpt1SubMtlAmt:int = obj["Rpt1SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.Rpt2SubMtlAmt:int = obj["Rpt2SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.Rpt3SubMtlAmt:int = obj["Rpt3SubMtlAmt"]
      """  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  """  
      self.PBRoleMarkup:int = obj["PBRoleMarkup"]
      """  Role Mark Up percentage  """  
      self.PackNum:str = obj["PackNum"]
      """  reference to Pack Slip number  """  
      self.DocChargeRate:int = obj["DocChargeRate"]
      """  Charge Rate  """  
      self.Rpt1ChargeRate:int = obj["Rpt1ChargeRate"]
      """  Charge Rate  """  
      self.Rpt2ChargeRate:int = obj["Rpt2ChargeRate"]
      """  Charge Rate  """  
      self.Rpt3ChargeRate:int = obj["Rpt3ChargeRate"]
      """  Charge Rate  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  in the Reporting currency  """  
      self.ToDelete:bool = obj["ToDelete"]
      """  Field to be deleted in Invoice Review, means that the related transaction will be skipped in the Recalculation of the Invoice  """  
      self.UpdatedAmt:bool = obj["UpdatedAmt"]
      """  Flag indicated that the amount has been updated in the Invoice Review program  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  copy from LaborDtl.TimeTypCd  """  
      self.ParentInvoiceLine:int = obj["ParentInvoiceLine"]
      """  Reference to the Parent Line from the Ceiling Line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.Comment:str = obj["Comment"]
      """  Line Comment  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  OrderRelNum  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  PriceListCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.DspCPMarkUpAmt:int = obj["DspCPMarkUpAmt"]
      self.DspCPMarkUpPrc:int = obj["DspCPMarkUpPrc"]
      self.DspCPTotalAmt:int = obj["DspCPTotalAmt"]
      self.DspLbrAssemblySeq:int = obj["DspLbrAssemblySeq"]
      self.DspLbrJobNum:str = obj["DspLbrJobNum"]
      self.DspLbrOprSeq:int = obj["DspLbrOprSeq"]
      self.DspMtlAssemblySeq:int = obj["DspMtlAssemblySeq"]
      self.DspMtlJobNum:str = obj["DspMtlJobNum"]
      self.DspMtlOprSeq:int = obj["DspMtlOprSeq"]
      self.DspSubAssemblySeq:int = obj["DspSubAssemblySeq"]
      self.DspSubJobNum:str = obj["DspSubJobNum"]
      self.DspSubOprSeq:int = obj["DspSubOprSeq"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      """  Phase Description  """  
      self.Rpt1TotLineAmt:int = obj["Rpt1TotLineAmt"]
      self.Rpt2TotLineAmt:int = obj["Rpt2TotLineAmt"]
      self.Rpt3TotLineAmt:str = obj["Rpt3TotLineAmt"]
      self.TotLineAmt:int = obj["TotLineAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocTotLineAmt:int = obj["DocTotLineAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  """  
      self.TmpInvcNum:int = obj["TmpInvcNum"]
      """  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  """  
      self.DspProjectInvcNum:str = obj["DspProjectInvcNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Actual Invoice date  """  
      self.DspInvoiceNum:int = obj["DspInvoiceNum"]
      self.DspTempInvcNum:int = obj["DspTempInvcNum"]
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.PrcStatus:str = obj["PrcStatus"]
      """  A = Approved, P = Posted, empty - review  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  """  
      self.TmpInvcNum:int = obj["TmpInvcNum"]
      """  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  """  
      self.ConReference:str = obj["ConReference"]
      """  Contract Reference  """  
      self.TmpInvcDate:str = obj["TmpInvcDate"]
      """  Date the user entered in Invoice Preparation form  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Actual Invoice date  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the Contract  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  """  
      self.PBFeePrjType:str = obj["PBFeePrjType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      """  P = Percentage, F = Fixed Amount  """  
      self.PBFeePrjApply:str = obj["PBFeePrjApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      """  F = First Invoice Only, A = All Invoices.  """  
      self.PBFeePrjCharge:int = obj["PBFeePrjCharge"]
      """  Project Fee Charge  """  
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      """  Subcontract Fee Charge  """  
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      """  Material Fee Charge  """  
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      """  Labor Fee Charge  """  
      self.BdnAmt:int = obj["BdnAmt"]
      """  Burden Amount  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  Other Direct Coat Amount  """  
      self.SubAmt:int = obj["SubAmt"]
      """  Subcontract Amount  """  
      self.MtlAmt:int = obj["MtlAmt"]
      """  Material Amount  """  
      self.LbrAmt:int = obj["LbrAmt"]
      """  Labor Amount  """  
      self.PBFeeTotal:int = obj["PBFeeTotal"]
      """  Total Fee  """  
      self.PBFeePrjAmt:int = obj["PBFeePrjAmt"]
      """  Project Fee Amount  """  
      self.PBFeeSubAmt:int = obj["PBFeeSubAmt"]
      """  Subcontract Fee Amount  """  
      self.PBFeeMtlAmt:int = obj["PBFeeMtlAmt"]
      """  Material Fee Amount  """  
      self.PBFeeLbrAmt:int = obj["PBFeeLbrAmt"]
      """  Labor Fee Amount  """  
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      """  N = Net Cost, G = Gross Cost  """  
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      """  The percentage to be retained, this can be 0.  """  
      self.RetentionProc:str = obj["RetentionProc"]
      """  Retention Processing with a system list of options: M - Maximum of Contract Value, I - Invoice Value  """  
      self.PBFeeRetentionAmt:int = obj["PBFeeRetentionAmt"]
      """  Fee Retention Amount  """  
      self.PBFeeNettAmt:int = obj["PBFeeNettAmt"]
      """  Fee Nett Amount  """  
      self.InvcTotalSumAmt:int = obj["InvcTotalSumAmt"]
      """  Summa of elements amounts  """  
      self.InvcAddFeeAmt:int = obj["InvcAddFeeAmt"]
      """  Total amount plus Fee  """  
      self.InvcCutCeiling:int = obj["InvcCutCeiling"]
      """  Total reduced by Ceiling  """  
      self.InvcCutRetention:int = obj["InvcCutRetention"]
      """  Total redused by Retention  """  
      self.InvcTotal:int = obj["InvcTotal"]
      """  Final Total Invoice  """  
      self.PrcStatus:str = obj["PrcStatus"]
      """  A = Approved, P = Posted, empty - review  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  Parameter of the Invoice Preparation process  """  
      self.PBCeilingFee:int = obj["PBCeilingFee"]
      """  Fee Ceiling  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Total Ceiling  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Individual Ceilings on Suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Individual Ceilings on Employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Individual Ceilings on Role  """  
      self.OverCeilingFees:int = obj["OverCeilingFees"]
      """  OverCeiling Fees (negative)  """  
      self.OverCeilingTotalAmt:int = obj["OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt  """  
      self.RetentionAmt:int = obj["RetentionAmt"]
      """  Retention Amount  """  
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      """  Percentage of Progress Payment, for PP invoice only.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the invoice was approved for posting  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  Approved by user id  """  
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeLbrAmt:int = obj["DocPBFeeLbrAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeLbrAmt:int = obj["Rpt1PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeLbrAmt:int = obj["Rpt2PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeLbrAmt:int = obj["Rpt3PBFeeLbrAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeMtlAmt:int = obj["DocPBFeeMtlAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeMtlAmt:int = obj["Rpt1PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeMtlAmt:int = obj["Rpt2PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeMtlAmt:int = obj["Rpt3PBFeeMtlAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeSubAmt:int = obj["DocPBFeeSubAmt"]
      """  in the Project currency  """  
      self.Rpt1PBFeeSubAmt:int = obj["Rpt1PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeSubAmt:int = obj["Rpt2PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeSubAmt:int = obj["Rpt3PBFeeSubAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeePrjCharge:int = obj["DocPBFeePrjCharge"]
      """  in the Project currency  """  
      self.Rpt1PBFeePrjCharge:int = obj["Rpt1PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeePrjCharge:int = obj["Rpt2PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeePrjCharge:int = obj["Rpt3PBFeePrjCharge"]
      """  in the Reporting currency  """  
      self.DocPBFeeTotal:int = obj["DocPBFeeTotal"]
      """  in the Project currency  """  
      self.Rpt1PBFeeTotal:int = obj["Rpt1PBFeeTotal"]
      """  in the Reporting currency  """  
      self.Rpt2PBFeeTotal:int = obj["Rpt2PBFeeTotal"]
      """  in the Reporting currency  """  
      self.Rpt3PBFeeTotal:int = obj["Rpt3PBFeeTotal"]
      """  in the Reporting currency  """  
      self.DocLbrAmt:int = obj["DocLbrAmt"]
      """  in the Project currency  """  
      self.Rpt1LbrAmt:int = obj["Rpt1LbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt2LbrAmt:int = obj["Rpt2LbrAmt"]
      """  in the Reporting currency  """  
      self.Rpt3LbrAmt:int = obj["Rpt3LbrAmt"]
      """  in the Reporting currency  """  
      self.DocMtlAmt:int = obj["DocMtlAmt"]
      """  in the Project currency  """  
      self.Rpt1MtlAmt:int = obj["Rpt1MtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MtlAmt:int = obj["Rpt2MtlAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MtlAmt:int = obj["Rpt3MtlAmt"]
      """  in the Reporting currency  """  
      self.DocSubAmt:int = obj["DocSubAmt"]
      """  in the Project currency  """  
      self.Rpt1SubAmt:int = obj["Rpt1SubAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SubAmt:int = obj["Rpt2SubAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SubAmt:int = obj["Rpt3SubAmt"]
      """  in the Reporting currency  """  
      self.DocBdnAmt:int = obj["DocBdnAmt"]
      """  in the Project currency  """  
      self.Rpt1BdnAmt:int = obj["Rpt1BdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt2BdnAmt:int = obj["Rpt2BdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt3BdnAmt:int = obj["Rpt3BdnAmt"]
      """  in the Reporting currency  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  in the Project currency  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  in the Reporting currency  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  in the Reporting currency  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  in the Reporting currency  """  
      self.DocPBCeilingFee:int = obj["DocPBCeilingFee"]
      """  Fee Ceiling in the Project currency  """  
      self.Rpt1PBCeilingFee:int = obj["Rpt1PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.Rpt2PBCeilingFee:int = obj["Rpt2PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.Rpt3PBCeilingFee:int = obj["Rpt3PBCeilingFee"]
      """  Fee Ceiling in the Reporting currency  """  
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      """  in the Project currency  """  
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      """  in the Reporting currency  """  
      self.DocOverCeilingFees:int = obj["DocOverCeilingFees"]
      """  OverCeiling Fees (negative) in the Project currency  """  
      self.Rpt1OverCeilingFees:int = obj["Rpt1OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.Rpt2OverCeilingFees:int = obj["Rpt2OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.Rpt3OverCeilingFees:int = obj["Rpt3OverCeilingFees"]
      """  OverCeiling Fees (negative) in the Reporting currency  """  
      self.DocRetentionAmt:int = obj["DocRetentionAmt"]
      """  Retention Amount in the Project currency  """  
      self.Rpt1RetentionAmt:int = obj["Rpt1RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.Rpt2RetentionAmt:int = obj["Rpt2RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.Rpt3RetentionAmt:int = obj["Rpt3RetentionAmt"]
      """  Retention Amount in the Reporting currency  """  
      self.DocOverCeilingTotalAmt:int = obj["DocOverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Project currency  """  
      self.Rpt1OverCeilingTotalAmt:int = obj["Rpt1OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.Rpt2OverCeilingTotalAmt:int = obj["Rpt2OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.Rpt3OverCeilingTotalAmt:int = obj["Rpt3OverCeilingTotalAmt"]
      """  OverCeilingTotalAmt in the Reporting currency  """  
      self.DocPBFeeRetentionAmt:int = obj["DocPBFeeRetentionAmt"]
      """  Fee Retention Amount in the Project currency  """  
      self.Rpt1PBFeeRetentionAmt:int = obj["Rpt1PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.Rpt2PBFeeRetentionAmt:int = obj["Rpt2PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.Rpt3PBFeeRetentionAmt:int = obj["Rpt3PBFeeRetentionAmt"]
      """  Fee Retention Amount in the Reporting currency  """  
      self.DocPBFeeNettAmt:int = obj["DocPBFeeNettAmt"]
      """  Fee Nett Amount in the Project currency  """  
      self.Rpt1PBFeeNettAmt:int = obj["Rpt1PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.Rpt2PBFeeNettAmt:int = obj["Rpt2PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.Rpt3PBFeeNettAmt:int = obj["Rpt3PBFeeNettAmt"]
      """  Fee Nett Amount in the Reporting currency  """  
      self.DocInvcTotalSumAmt:int = obj["DocInvcTotalSumAmt"]
      """  Summa of elements amounts  in the Project currency  """  
      self.Rpt1InvcTotalSumAmt:int = obj["Rpt1InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.Rpt2InvcTotalSumAmt:int = obj["Rpt2InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.Rpt3InvcTotalSumAmt:int = obj["Rpt3InvcTotalSumAmt"]
      """  Summa of elements amounts  in the Reporting currency  """  
      self.DocInvcAddFeeAmt:int = obj["DocInvcAddFeeAmt"]
      """  Total amount plus Fee in the Project currency  """  
      self.Rpt1InvcAddFeeAmt:int = obj["Rpt1InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.Rpt2InvcAddFeeAmt:int = obj["Rpt2InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.Rpt3InvcAddFeeAmt:int = obj["Rpt3InvcAddFeeAmt"]
      """  Total amount plus Fee in the Reporting currency  """  
      self.DocInvcCutCeiling:int = obj["DocInvcCutCeiling"]
      """  Total reduced by Ceiling in the Project currency  """  
      self.Rpt1InvcCutCeiling:int = obj["Rpt1InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.Rpt2InvcCutCeiling:int = obj["Rpt2InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.Rpt3InvcCutCeiling:int = obj["Rpt3InvcCutCeiling"]
      """  Total reduced by Ceiling in the Reporting currency  """  
      self.DocInvcTotal:int = obj["DocInvcTotal"]
      """  Final Total Invoice in the Project currency  """  
      self.Rpt1InvcTotal:int = obj["Rpt1InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.Rpt2InvcTotal:int = obj["Rpt2InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.Rpt3InvcTotal:int = obj["Rpt3InvcTotal"]
      """  Final Total Invoice in the Reporting currency  """  
      self.SumLbrTotalAmt:int = obj["SumLbrTotalAmt"]
      """  Labor actual amount  """  
      self.SumMtlTotalAmt:int = obj["SumMtlTotalAmt"]
      """  Material actual amount  """  
      self.SumSubTotalAmt:int = obj["SumSubTotalAmt"]
      """  Subcontract actual amount  """  
      self.SumBdnAmt:int = obj["SumBdnAmt"]
      """  Burden actual amount  """  
      self.DocSumLbrTotalAmt:int = obj["DocSumLbrTotalAmt"]
      """  Labor actual amount in the Project currency  """  
      self.Rpt1SumLbrTotalAmt:int = obj["Rpt1SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.Rpt2SumLbrTotalAmt:int = obj["Rpt2SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.Rpt3SumLbrTotalAmt:int = obj["Rpt3SumLbrTotalAmt"]
      """  Labor actual amount in the Reporting currency  """  
      self.DocSumMtlTotalAmt:int = obj["DocSumMtlTotalAmt"]
      """  Material actual amount in the Project currency  """  
      self.Rpt1SumMtlTotalAmt:int = obj["Rpt1SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.Rpt2SumMtlTotalAmt:int = obj["Rpt2SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.Rpt3SumMtlTotalAmt:int = obj["Rpt3SumMtlTotalAmt"]
      """  Material actual amount in the Reporting currency  """  
      self.DocSumSubTotalAmt:int = obj["DocSumSubTotalAmt"]
      """  Subcontract actual amount in the Project currency  """  
      self.Rpt1SumSubTotalAmt:int = obj["Rpt1SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.Rpt2SumSubTotalAmt:int = obj["Rpt2SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.Rpt3SumSubTotalAmt:int = obj["Rpt3SumSubTotalAmt"]
      """  Subcontract actual amount in the Reporting currency  """  
      self.DocSumBdnAmt:int = obj["DocSumBdnAmt"]
      """  in the Project currency  """  
      self.Rpt1SumBdnAmt:int = obj["Rpt1SumBdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt2SumBdnAmt:int = obj["Rpt2SumBdnAmt"]
      """  in the Reporting currency  """  
      self.Rpt3SumBdnAmt:int = obj["Rpt3SumBdnAmt"]
      """  in the Reporting currency  """  
      self.DocPBFeePrjAmt:int = obj["DocPBFeePrjAmt"]
      """  Project Fee Amount in Document Currency  """  
      self.Rpt1PBFeePrjAmt:int = obj["Rpt1PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 1  """  
      self.Rpt2PBFeePrjAmt:int = obj["Rpt2PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 2  """  
      self.Rpt3PBFeePrjAmt:int = obj["Rpt3PBFeePrjAmt"]
      """  Project Fee Amount in Report Currency 3  """  
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      """   Other Direct Cost Fee Type
List of options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      """   Other Direct Cost Fee Apply Type
List of options: F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied  """  
      self.PBFeeMiscAmt:int = obj["PBFeeMiscAmt"]
      """  Calculated ODC Fee amount  """  
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Project currency  """  
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      """  Other Direct Cost Fee value being applied in the Reporting currency  """  
      self.DocPBFeeMiscAmt:int = obj["DocPBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Project currency  """  
      self.Rpt1PBFeeMiscAmt:int = obj["Rpt1PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.Rpt2PBFeeMiscAmt:int = obj["Rpt2PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.Rpt3PBFeeMiscAmt:int = obj["Rpt3PBFeeMiscAmt"]
      """  Calculated ODC Fee amount in the Reporting currency  """  
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      """  Retention percentage. How this is used is dependent on RetentionProc field.  """  
      self.Updated:bool = obj["Updated"]
      """  Flag indicated that one of its lines has been updated or deleted in the Invoice Review program  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Indicates if invoice should be auto printed  """  
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      """  Fee Invoice Text  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.PPAllOrderLines:bool = obj["PPAllOrderLines"]
      """  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  """  
      self.PPAllPrjJobs:bool = obj["PPAllPrjJobs"]
      """  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      """  Flag indicates if AR invoices are allowed to be generated even if the element is over the predefined ceiling (limit), also indicates if the invoice amount should stay limited or not when ceiling exists. It is copied from the current value of Project flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  Base Currency ID  """  
      self.DspInvoiceNum:int = obj["DspInvoiceNum"]
      self.DspTempInvcNum:int = obj["DspTempInvcNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.ProjectIDConReference:str = obj["ProjectIDConReference"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBGInvoiceListTableset:
   def __init__(self, obj):
      self.PBGInvcHeadList:list[Erp_Tablesets_PBGInvcHeadListRow] = obj["PBGInvcHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PBGInvoiceTableset:
   def __init__(self, obj):
      self.PBGInvcHead:list[Erp_Tablesets_PBGInvcHeadRow] = obj["PBGInvcHead"]
      self.PBGInvcBdn:list[Erp_Tablesets_PBGInvcBdnRow] = obj["PBGInvcBdn"]
      self.PBGInvcDtlFF:list[Erp_Tablesets_PBGInvcDtlFFRow] = obj["PBGInvcDtlFF"]
      self.PBGInvcDtlTC:list[Erp_Tablesets_PBGInvcDtlTCRow] = obj["PBGInvcDtlTC"]
      self.PBInvoicedAmt:list[Erp_Tablesets_PBInvoicedAmtRow] = obj["PBInvoicedAmt"]
      self.PBPrjInvcPhaseList:list[Erp_Tablesets_PBPrjInvcPhaseListRow] = obj["PBPrjInvcPhaseList"]
      self.PBProjectsList:list[Erp_Tablesets_PBProjectsListRow] = obj["PBProjectsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PBInvoicedAmtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  Related To File  """  
      self.TranKey:str = obj["TranKey"]
      """  Transaction Key  """  
      self.DocPrepAmt:int = obj["DocPrepAmt"]
      """  Amount strored by Invoice Preparation before Posting ,used to appropriate compare with Ceiling  """  
      self.PrepOverCeiling:int = obj["PrepOverCeiling"]
      """  Preparation over ceiling in Base curency  """  
      self.DocPrepOverCeiling:int = obj["DocPrepOverCeiling"]
      """  Preparation over ceiling in Document curency  """  
      self.GenOverCeiling:int = obj["GenOverCeiling"]
      """  Generated Over ceiling in Base currency  """  
      self.DocGenOverCeiling:int = obj["DocGenOverCeiling"]
      """  Generated Over ceiling in Document currency  """  
      self.PostOverCeiling:int = obj["PostOverCeiling"]
      """  Posted Over Ceiling in Base currency  """  
      self.DocPostOverCeiling:int = obj["DocPostOverCeiling"]
      """  Posted Over Ceiling in Document currency  """  
      self.GenAmt:int = obj["GenAmt"]
      """  Ceiling Generated Consumed in Base currency  """  
      self.DocGenAmt:int = obj["DocGenAmt"]
      """  Ceiling Generated Consumed in Document currency  """  
      self.PostAmt:int = obj["PostAmt"]
      """  Ceiling Posted Consumed in Base currency  """  
      self.DocPostAmt:int = obj["DocPostAmt"]
      """  Ceiling Posted Consumed in Document currency  """  
      self.PrepAmt:int = obj["PrepAmt"]
      """  Ceiling Preparation Consumed in Document currency  """  
      self.CeilingLimit:int = obj["CeilingLimit"]
      """  Ceiling Limit in Base currency  """  
      self.DocCeilingLimit:int = obj["DocCeilingLimit"]
      """  Ceiling Limit in Project Currency  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice Number. It's zero for preparation and total values for whole project  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Tax Category ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBPrjInvcPhaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ProjectID:str = obj["ProjectID"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.PhaseID:str = obj["PhaseID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PBProjectsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ProjectID:str = obj["ProjectID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPBGInvoiceTableset:
   def __init__(self, obj):
      self.PBGInvcHead:list[Erp_Tablesets_PBGInvcHeadRow] = obj["PBGInvcHead"]
      self.PBGInvcBdn:list[Erp_Tablesets_PBGInvcBdnRow] = obj["PBGInvcBdn"]
      self.PBGInvcDtlFF:list[Erp_Tablesets_PBGInvcDtlFFRow] = obj["PBGInvcDtlFF"]
      self.PBGInvcDtlTC:list[Erp_Tablesets_PBGInvcDtlTCRow] = obj["PBGInvcDtlTC"]
      self.PBInvoicedAmt:list[Erp_Tablesets_PBInvoicedAmtRow] = obj["PBInvoicedAmt"]
      self.PBPrjInvcPhaseList:list[Erp_Tablesets_PBPrjInvcPhaseListRow] = obj["PBPrjInvcPhaseList"]
      self.PBProjectsList:list[Erp_Tablesets_PBProjectsListRow] = obj["PBProjectsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   projectID
   invoiceNum
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PBGInvoiceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PBGInvoiceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PBGInvoiceTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDataByProjectID_input:
   """ Required : 
   ipProjectID
   ipConInvMeth
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The ProjectID.  """  
      self.ipConInvMeth:str = obj["ipConInvMeth"]
      """  The ConInvMeth.  """  
      pass

class GetDataByProjectID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PBGInvoiceTableset] = obj["returnObj"]
      pass

class GetDataByTempInvoiceNum_input:
   """ Required : 
   ipProjectID
   ipConInvMeth
   ipInvoiceNum
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The ProjectID.  """  
      self.ipConInvMeth:str = obj["ipConInvMeth"]
      """  The ConInvMeth.  """  
      self.ipInvoiceNum:int = obj["ipInvoiceNum"]
      """  The Invoice Num.  """  
      pass

class GetDataByTempInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opInvoiceNum:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_PBGInvoiceListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPBGInvcBdn_input:
   """ Required : 
   ds
   projectID
   invoiceNum
   recSeq
   bdnSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.recSeq:int = obj["recSeq"]
      self.bdnSetID:str = obj["bdnSetID"]
      pass

class GetNewPBGInvcBdn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPBGInvcDtlFF_input:
   """ Required : 
   ds
   projectID
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewPBGInvcDtlFF_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPBGInvcDtlTC_input:
   """ Required : 
   ds
   projectID
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewPBGInvcDtlTC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPBGInvcHead_input:
   """ Required : 
   ds
   projectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      pass

class GetNewPBGInvcHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPBInvoicedAmt_input:
   """ Required : 
   ds
   projectID
   invoiceNum
   relatedToFile
   tranKey
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.tranKey:str = obj["tranKey"]
      pass

class GetNewPBInvoicedAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePBGInvcHead
   whereClausePBGInvcBdn
   whereClausePBGInvcDtlFF
   whereClausePBGInvcDtlTC
   whereClausePBInvoicedAmt
   whereClausePBPrjInvcPhaseList
   whereClausePBProjectsList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePBGInvcHead:str = obj["whereClausePBGInvcHead"]
      self.whereClausePBGInvcBdn:str = obj["whereClausePBGInvcBdn"]
      self.whereClausePBGInvcDtlFF:str = obj["whereClausePBGInvcDtlFF"]
      self.whereClausePBGInvcDtlTC:str = obj["whereClausePBGInvcDtlTC"]
      self.whereClausePBInvoicedAmt:str = obj["whereClausePBInvoicedAmt"]
      self.whereClausePBPrjInvcPhaseList:str = obj["whereClausePBPrjInvcPhaseList"]
      self.whereClausePBProjectsList:str = obj["whereClausePBProjectsList"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PBGInvoiceTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPBGInvoiceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPBGInvoiceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PBGInvoiceTableset] = obj["ds"]
      pass

      """  output parameters  """  

