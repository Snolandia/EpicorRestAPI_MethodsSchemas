import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandEntrySvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries",headers=creds) as resp:
           return await resp.json()

async def post_DemandEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company, DemandContractNum, DemandHeadSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandEntry item
   Description: Calls GetByID to retrieve the DemandEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company, DemandContractNum, DemandHeadSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandEntry for the service
   Description: Calls UpdateExt to update DemandEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company, DemandContractNum, DemandHeadSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandEntry item
   Description: Call UpdateExt to delete DemandEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandDetails(Company, DemandContractNum, DemandHeadSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetails",headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandDetail item
   Description: Calls GetByID to retrieve the DemandDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandMiscChgDHs(Company, DemandContractNum, DemandHeadSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgDHs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgDHs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgDHs",headers=creds) as resp:
           return await resp.json()

async def get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgDH item
   Description: Calls GetByID to retrieve the DemandMiscChgDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgDH1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails",headers=creds) as resp:
           return await resp.json()

async def post_DemandDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandDetail item
   Description: Calls GetByID to retrieve the DemandDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandDetail for the service
   Description: Calls UpdateExt to update DemandDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandDetail item
   Description: Call UpdateExt to delete DemandDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgs(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgs",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChg item
   Description: Calls GetByID to retrieve the DemandMiscChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChg1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandSchedules(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandSchedules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandSchedules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandSchedules",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandSchedule item
   Description: Calls GetByID to retrieve the DemandSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandSchedule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs",headers=creds) as resp:
           return await resp.json()

async def post_DemandMiscChgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChg item
   Description: Calls GetByID to retrieve the DemandMiscChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandMiscChg for the service
   Description: Calls UpdateExt to update DemandMiscChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandMiscChg item
   Description: Call UpdateExt to delete DemandMiscChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandSchedules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandSchedules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandSchedules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules",headers=creds) as resp:
           return await resp.json()

async def post_DemandSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandSchedule item
   Description: Calls GetByID to retrieve the DemandSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandSchedule for the service
   Description: Calls UpdateExt to update DemandSchedule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandSchedule item
   Description: Call UpdateExt to delete DemandSchedule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgDHs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgDHs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgDHs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs",headers=creds) as resp:
           return await resp.json()

async def post_DemandMiscChgDHs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgDHs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgDH item
   Description: Calls GetByID to retrieve the DemandMiscChgDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandMiscChgDH for the service
   Description: Calls UpdateExt to update DemandMiscChgDH. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandMiscChgDH item
   Description: Call UpdateExt to delete DemandMiscChgDH item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDemandHead, whereClauseDemandDetail, whereClauseDemandMiscChg, whereClauseDemandSchedule, whereClauseDemandMiscChgDH, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseDemandHead=" + whereClauseDemandHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandDetail=" + whereClauseDemandDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandMiscChg=" + whereClauseDemandMiscChg
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandSchedule=" + whereClauseDemandSchedule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandMiscChgDH=" + whereClauseDemandMiscChgDH
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(demandContractNum, demandHeadSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "demandContractNum=" + demandContractNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "demandHeadSeq=" + demandHeadSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartAndConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartForConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildDisplayAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildDisplayAddress
   Description: Format a list of addresses into a display string.
   OperationID: BuildDisplayAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildDisplayAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildDisplayAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCreateCycleListValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCreateCycleListValues
   Description: Public method to return the list values of getCreateCycleList
   OperationID: GetCreateCycleListValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCreateCycleListValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreateCycleListValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCreateNewOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCreateNewOrder
   Description: Update Demand Header information when the Bill To.
   OperationID: ChangeCreateNewOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCreateNewOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCreateNewOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailCustomerPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailCustomerPrice
   Description: Update UnitPrice Based on Customer Price.
   OperationID: ChangeDemandDetailCustomerPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailCustomerPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailCustomerPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailDemandContractLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailDemandContractLine
   Description: Update Demand Detail information when the Demand Contract Line is changed.
   OperationID: ChangeDemandDetailDemandContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailDemandContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailDemandContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailInternalPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailInternalPrice
   Description: Update UnitPrice Based on Internal Price.
   OperationID: ChangeDemandDetailInternalPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailInternalPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailInternalPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailMktgCamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDemandDetailMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailPartNum
   Description: Update partnum on the DmdCntDtl.
   OperationID: ChangeDemandDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailRevisionNum
   Description: Update Demand Detail information when the Part Revision Number is changed.
   OperationID: ChangeDemandDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailUnitPrice
   Description: Update UnitPrice Base.
   OperationID: ChangeDemandDetailUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailUOM
   Description: Update Demand Detail information when the SalesUM changes.
   OperationID: ChangeDemandDetailUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadBTCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadBTCustID
   Description: Update Demand Header information when the Bill To.
   OperationID: ChangeDemandHeadBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadCancelPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadCancelPO
   Description: Update Demand Header information when the Cancel PO flag changes.
   OperationID: ChangeDemandHeadCancelPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadCancelPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadCancelPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadDemandContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadDemandContract
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadDemandContractNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadDemandContractNum
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadERSOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadERSOrder
   Description: Update Demand Header information when the ERS Order changes.
   OperationID: ChangeDemandHeadERSOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadERSOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadERSOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandHead record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandHeadShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadShipToNum
   Description: Update Demand Header information when the Ship To Num changes.
   OperationID: ChangeDemandHeadShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadUseOTS
   Description: Method to call when changing the UseOTS field the DemandHead record.
Refreshes the address list and contact info
   OperationID: ChangeDemandHeadUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleCreateShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleCreateShipToNum
   Description: Update DemandScheduleCreate information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleCreateShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleCreateShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleCreateShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleMarkForNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleMarkForNum
   Description: Update DemandSchedule information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeDemandScheduleMarkForNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMarkForNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMarkForNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleMFCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleMFCustID
   Description: Method to call when changing the Mark For Customer ID on the DemandSchedule record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleNeedByDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleNeedByDate
   Description: Calculate the DemandSchedule Ship Date when the NeedByDate is changed.
   OperationID: ChangeDemandScheduleNeedByDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleNeedByDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleNeedByDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleDeliveryDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleDeliveryDays
   Description: Calculate the DemandSchedule ShipDate or NeedBy Date when the DeliveryDays are changed.
   OperationID: ChangeDemandScheduleDeliveryDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleDeliveryDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleDeliveryDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleOTSDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleOTSDetails
   Description: Method to call when changing the OTS fields the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleOTSDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleOTSDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleOTSDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandSchedulePlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandSchedulePlant
   Description: Update DemandSchedule information with values from the Plant when the Plant is changed.
   OperationID: ChangeDemandSchedulePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandSchedulePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandSchedulePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleReqDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleReqDate
   Description: Calculate the DemandSchedule NeedByDate when the Ship Date (ReqDate) is changed.
   OperationID: ChangeDemandScheduleReqDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleReqDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleReqDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleSellingReqQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleSellingReqQty
   Description: Update Demand Schedule information when the Selling Req Qty is changed.
   OperationID: ChangeDemandScheduleSellingReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandSchedule record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleShipToNum
   Description: Update DemandSchedule information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleUseOTMF(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleUseOTMF
   Description: Method to call when changing the UseOTMF field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleUseOTS
   Description: Method to call when changing the UseOTS field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscAmount
   Description: Update Order Miscellaneous information when the amount changes.
   OperationID: ChangeMiscAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscCode
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field.
Also allows DemandMiscChgDH and DemandMiscChg to use the same code
   OperationID: ChangeMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscPercent
   Description: Update Order Miscellaneous information when the percentage was changed.
   OperationID: ChangeMiscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartRevisionChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartRevisionChange
   Description: The method is to be run on leave of the PartNum and Revision fields
before the ChangePart, ChangeRevision, or Update methods are run.
When run before CreateOrderFromQuote, the Part Number expected is the part number
from the quote.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartRevisionChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartRevisionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartRevisionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseAllSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseAllSchedules
   Description: Close All Schedules.
   OperationID: CloseAllSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseAllSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAllSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseDemandDetail
   Description: Closes the Demand detail and sub-table (DemandSchedule).
   OperationID: CloseDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseDemandHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseDemandHead
   Description: Closes the Demand Header and sub-tables (DemandDetail and DemandSchedule).
   OperationID: CloseDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseDemandSchedule
   Description: Closes the Demand Schedule record.
   OperationID: CloseDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDemandDetailFromContractLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDemandDetailFromContractLines
   Description: Create DemandDetail records from the contract lines selected.  This method
will create a DemandDetail record for each contract line where SelectedForDemand
is true.  After this method is run the GetRows or GetByID method should be called
so the dataset has the new DemandDetail records.
   OperationID: CreateDemandDetailFromContractLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDemandDetailFromContractLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDemandDetailFromContractLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteScheduleByScheduleNumberKeepHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteScheduleByScheduleNumberKeepHeader
   Description: Delete Schedule by number, but return the existing header, details, and schedule rows
   OperationID: DeleteScheduleByScheduleNumberKeepHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteScheduleByScheduleNumberKeepHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteScheduleByScheduleNumberKeepHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteScheduleByScheduleNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteScheduleByScheduleNumber
   Description: Deletes DemandSchedule records by Schedule Number.  All DemandSchedule records
where the Schedule Number equals the number passed in will be deleted.
cReturnMessage will return a message of how many records were deleted.
   OperationID: DeleteScheduleByScheduleNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteScheduleByScheduleNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteScheduleByScheduleNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EDIHeaderValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EDIHeaderValidate
   Description: Calls the method Process Demand To create a Sales Order.
   OperationID: EDIHeaderValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIHeaderValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIHeaderValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandContractDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandContractDtl
   Description: Get Demand Contract Detail lines for Create Demand Detail from Demand Contract
lines functionality.  The contract lines returned can be selected by the user
to indicate what contract lines to create Demand Detail records from.
   OperationID: GetDemandContractDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandDtlReview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandDtlReview
   Description: Creates records in the DemandReview DataSet so the user can review the impact
of the demand schedule prior to accepting or rejecting it.
   OperationID: GetDemandDtlReview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandDtlReview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandDtlReview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandMatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandMatching
   Description: Creates records in the DemandMatching DataSet so the user can manually match
DemandSchedule records to existing OrderRel records.
   OperationID: GetDemandMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandScheduleCreate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandScheduleCreate
   Description: Creates a record in the DemandScheduleCreate datatable to store the parameters
needed to mass-build DemandSchedule records for a DemandDetail line.
   OperationID: GetDemandScheduleCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandScheduleCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandScheduleCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom Search
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetListCustomWithPaging(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustomWithPaging
   Description: Custom Search that handles server paging
   OperationID: Get_GetListCustomWithPaging
      :param whereClause: Desc: The search criteria   Required: True   Allow empty value : True
      :param pageSize: Desc: Size of a page   Required: True
      :param absolutePage: Desc: The absolute page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustomWithPaging_output
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceDiscrepancy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceDiscrepancy
   Description: Check if the difference between the InternalPrice and EDIUnitPrice (Customer Price) is less than the value defined in
the PriceTolerance field of the ShipTo or Customer tables.
   OperationID: GetPriceDiscrepancy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceDiscrepancy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceDiscrepancy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassCreateDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassCreateDemandSchedule
   Description: Creates DemandSchedule records based on user criteria entered in the
DemandScheduleCreate datatable. At the end refresh the
DemandHead/DemandDetail/DemandSchedule for a specific Demand
Contract Line to avoid perform a GetByID that consumes a lot of time.
   OperationID: MassCreateDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassCreateDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassCreateDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenDemandDetail
   Description: Opens the Demand detail.
   OperationID: OpenDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenDemandHeadKeepDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenDemandHeadKeepDemandDetail
   Description: Opens the Demand Header and keeps the existing Details and Schedules.
   OperationID: OpenDemandHeadKeepDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandHeadKeepDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandHeadKeepDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenDemandHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenDemandHead
   Description: Opens the Demand Header.
   OperationID: OpenDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenDemandSchedule
   Description: Opens the Demand Schedule record.
   OperationID: OpenDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessDemand
   Description: Process the demand.  This will accept or reject DemandHead, DemandDetail, and
DemandSchedule records and create/update Forecasts or Orders.
cReturnMessage contains an informational message that lets the user know the process
has completed and if any errors were written to the DemandLog table.
   OperationID: ProcessDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessMatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessMatching
   Description: Updates the Order fields in DemandSchedule with the values from DemandScheduleToMatch.
   OperationID: ProcessMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectDemandDetail
   Description: Rejects the Demand detail and sub-table (DemandSchedule).
   OperationID: RejectDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectDemandHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectDemandHead
   Description: Rejects the Demand Header and sub-tables (DemandDetail and DemandSchedule).
   OperationID: RejectDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectDemandScheduleKeepSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectDemandScheduleKeepSchedules
   Description: Reject a Demand Schedule but return previously existing schedules
   OperationID: RejectDemandScheduleKeepSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandScheduleKeepSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandScheduleKeepSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectDemandSchedule
   Description: Rejects the Demand Schedule record.
   OperationID: RejectDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToProcess
   Description: Set the Ready to Process flag on the Demand Header.
This was created mainly for web services.
   OperationID: SetReadyToProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockDemand
   Description: Provide a way to unlock a demand entry for cases when ESC fails.
   OperationID: UnlockDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnrejectDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnrejectDemandDetail
   Description: Unrejects the Demand detail.
   OperationID: UnrejectDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnrejectDemandHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnrejectDemandHead
   Description: UnReject the Demand Header.
   OperationID: UnrejectDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnrejectDemandScheduleKeepSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnrejectDemandScheduleKeepSchedules
   Description: Unreject a Demand Schedule but return the other existing schedules.
   OperationID: UnrejectDemandScheduleKeepSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandScheduleKeepSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandScheduleKeepSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnrejectDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnrejectDemandSchedule
   Description: Unrejects the Demand Schedule record.
   OperationID: UnrejectDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartValidation
   OperationID: PartValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationChangePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationChangePart
   Description: Update Order details information when the Part Number is changed by Configuration Part Creation.
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationRefreshQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationRefreshQty
   Description: Update PriceList Qty breaks and set new unit price on those
when the Part Number is changed by Document Rule.
   OperationID: ConfigurationRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandHeadData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandHeadData
   Description: this method returns DemandHead Records with search criteria for DemandEntry LandingPage
   OperationID: GetDemandHeadData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandHeadData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandHeadData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandMiscChg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandMiscChg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandSchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandMiscChgDH(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandMiscChgDH
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgDH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgDH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgDH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandMiscChgDHRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandMiscChgRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandScheduleRow] = obj["value"]
      pass

class Erp_Tablesets_DemandDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandDetail is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The contract line this demand line is for.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderDtl record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The OrderDtl record this demand detail is linked to.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other sales order detail records that have been created by this demand.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which the line item detail record is associated with. This is part of the foreign key to QuoteHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number to which this line was related. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.ScheduleType:str = obj["ScheduleType"]
      """  The schedule type from the trading partner.  Reference only.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandDetail has been rejected by the user.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record has been written to an OrderDtl.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the DemandDetail record is in a "open or closed" status.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand entry if the CRM module is installed.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Only used for audit purposes for EDI.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Only used for audit purposes for EDI.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Only used for audit purposes for EDI.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.EDIUnitPrice:int = obj["EDIUnitPrice"]
      """  The Incoming EDI Unit Price.  """  
      self.CumulativeQty:int = obj["CumulativeQty"]
      """  The total quantity that has been received according to the training partner data  """  
      self.CumulativeDate:str = obj["CumulativeDate"]
      """  The date when the trading partner calculated the cumulative quantity field  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  A qty that will create a new reconciliation adjustment.  """  
      self.StartCumDate:str = obj["StartCumDate"]
      """  The date since the trading partner has been accumulating the quantities.  """  
      self.LastShipmentID:int = obj["LastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.LastShipmentQty:int = obj["LastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.LastShipmentDate:str = obj["LastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.LastMasterPack:int = obj["LastMasterPack"]
      """  Last Master Pack ID  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Contains the internal system unit price in a foreign currency  """  
      self.DocEDIUnitPrice:int = obj["DocEDIUnitPrice"]
      """  Contains the Customer Price in a foreign currency  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """  This is the Internal Price assigned by the system calculated from the part sales price or a price list. It will be used when the Demand Contract is using Internal Pricing.  """  
      self.DocInternalPrice:int = obj["DocInternalPrice"]
      """  The doc currency value of the internal price  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.TPQuoteNum:int = obj["TPQuoteNum"]
      """  Trading Partner Quote Number. This is not an internal quote number, it is the quote sent by the trading partner.  """  
      self.TPQuoteLine:int = obj["TPQuoteLine"]
      """  Trading Partner Quote Line Number. This is not related to an internal quote, it is sent by the trading partner.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt1InternalPrice:int = obj["Rpt1InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt2InternalPrice:int = obj["Rpt2InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt3InternalPrice:int = obj["Rpt3InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt1EDIUnitPrice:int = obj["Rpt1EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.Rpt2EDIUnitPrice:int = obj["Rpt2EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.Rpt3EDIUnitPrice:int = obj["Rpt3EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.BlockProcLine:bool = obj["BlockProcLine"]
      """  Indicates if current line is blocked for processing.  """  
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  This is field is similar to DemandContract. The field CUMMSetting helps to choose how the DemandReconciliation will open.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.EnableCreateSchedule:bool = obj["EnableCreateSchedule"]
      """  Indicates if the Create Demand Schedule option is available.  """  
      self.EnableDeleteReleases:bool = obj["EnableDeleteReleases"]
      self.EnableDeleteSchedule:bool = obj["EnableDeleteSchedule"]
      """  Indicates if the Delete Schedule by Schedule Number option is available.  """  
      self.EnableLog:bool = obj["EnableLog"]
      """  Indicates if the Log action item is available.  """  
      self.EnableOnlyPart:bool = obj["EnableOnlyPart"]
      """  This field is true is Demand Detail is posted or has link with SO.  """  
      self.EnableOverrideReject:bool = obj["EnableOverrideReject"]
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available.  """  
      self.EnableRevMatch:bool = obj["EnableRevMatch"]
      """  Indicates if the Review and Matching options are available.  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.MultipleXRef:bool = obj["MultipleXRef"]
      """  True when the XRefPartNum has multiple references.  """  
      self.PriceDiscrepancy:bool = obj["PriceDiscrepancy"]
      """  True when exists a Price Discrepancy beetwen UnitPrice and EDIUnitPrice  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.Configured:str = obj["Configured"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DemandContractDtlSalesUM:str = obj["DemandContractDtlSalesUM"]
      self.DemandContractHdrCUMMSetting:str = obj["DemandContractHdrCUMMSetting"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The OrderHed record this demand is linked to.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is a mandatory field used to enter the customers Purchase Order Number.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.AcceptType:str = obj["AcceptType"]
      """   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.Accepted:bool = obj["Accepted"]
      """  Indicates if this demand has been accepted or not.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandHead has been rejected by the user.  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI.  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  Do Not Process  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Flag at the Header Level that indicate that the demand can be process.  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  new orders will be created when it is set to true  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  Sales Order linked to this Demand  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.BatchNum:str = obj["BatchNum"]
      """  EDI Batch Control Number  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates if the One Time Shipto information is to be used.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.CustAddrList:str = obj["CustAddrList"]
      """  Holds a string with the customer address  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.BTCustID:str = obj["BTCustID"]
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BTAddressList:str = obj["BTAddressList"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.EnableGetLines:bool = obj["EnableGetLines"]
      """  Indicates if the Get Contract Lines option is available.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available  """  
      self.EnableProcess:bool = obj["EnableProcess"]
      """  Indicates if the Process action item is available.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.EnableLog:bool = obj["EnableLog"]
      self.DemandSchedAvail:bool = obj["DemandSchedAvail"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Indicates if the recently created order should be placed on hold. Defaults from Contract.  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Ship To Address List.  """  
      self.EDITran_Type:str = obj["EDITran_Type"]
      """  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  """  
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  """  
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  Country name  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      """  Description of the reservation priority. Example "High".  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsDescription:str = obj["TermsDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The OrderHed record this demand is linked to.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is a mandatory field used to enter the customers Purchase Order Number.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.AcceptType:str = obj["AcceptType"]
      """   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.Accepted:bool = obj["Accepted"]
      """  Indicates if this demand has been accepted or not.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandHead has been rejected by the user.  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI.  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  Do Not Process  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Flag at the Header Level that indicate that the demand can be process.  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  new orders will be created when it is set to true  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  Sales Order linked to this Demand  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.BatchNum:str = obj["BatchNum"]
      """  EDI Batch Control Number  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  Ship the good by this time  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS ShipToNum  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates if the One Time Shipto information is to be used.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.EnableProcess:bool = obj["EnableProcess"]
      """  Indicates if the Process action item is available.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  """  
      self.OpenContract:bool = obj["OpenContract"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Indicates if the recently created order should be placed on hold. Defaults from Contract.  """  
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  OTS Country Description  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  OTS Tax Region Description  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Ship To Address List.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BTAddressList:str = obj["BTAddressList"]
      self.BTCustID:str = obj["BTCustID"]
      self.CustAddrList:str = obj["CustAddrList"]
      """  Holds a string with the customer address  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandSchedAvail:bool = obj["DemandSchedAvail"]
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.EDITran_Type:str = obj["EDITran_Type"]
      """  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  """  
      self.EnableGetLines:bool = obj["EnableGetLines"]
      """  Indicates if the Get Contract Lines option is available.  """  
      self.EnableLog:bool = obj["EnableLog"]
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryDescription_:str = obj["OTSCountryDescription_"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgDHRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand misc charge is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The DemandHead this charge is for.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.Quoting:str = obj["Quoting"]
      """  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand misc charge is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The DemandHead this charge is for.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.Quoting:str = obj["Quoting"]
      """  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.GroupID:str = obj["GroupID"]
      """  All invoices belong to a group until the group is closed. The GroupID is assigned by the user.  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  """  
      self.MarkForNum:str = obj["MarkForNum"]
      """  The Mark For to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.DeliveryDays:int = obj["DeliveryDays"]
      """  The delivery days required for the shipment to reach its destination.  Defaults from Customer.DemandDeliveryDays or ShipTo.DemandDeliveryDays.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.DemandType:str = obj["DemandType"]
      """   The type of demand this line represents.  Values are:
InForecast - Incoming Forecast (Forecasts)
InUnfirm - Incoming Unfirm Releases (Unfirm OrderRel)
InShSched - Incoming Shipping Schedule (Firm OrderRel)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales order number of the OrderRel record this DemandSchedule is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number of the OrderRel record this DemandSchedule is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Sales order release number of the OrderRel record this DemandSchedule is linked to.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandSchedule has been rejected by the user.  """  
      self.RAN:str = obj["RAN"]
      """  RAN Number.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  """  
      self.DemandReference:str = obj["DemandReference"]
      """  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record has been written to an OrderDtl.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OpenSchedule:bool = obj["OpenSchedule"]
      """  Indicates if this schedule is open.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.DocumentName:str = obj["DocumentName"]
      """  The document that initiated the demand.  Will be blank when the demand is manually entered.  """  
      self.ForecastEndDate:str = obj["ForecastEndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.Location:str = obj["Location"]
      """  The location within the customer shipto address.  For future use.  """  
      self.TransportID:str = obj["TransportID"]
      """  The code of the transport routing/time. For future use.  """  
      self.ShipbyTime:int = obj["ShipbyTime"]
      """  Ship the good by this time.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used.  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.SubShipTo:str = obj["SubShipTo"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  """  
      self.ShipRouting:str = obj["ShipRouting"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Last update to the demand schedule record  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  Bookdate of the related bookrel by the sales order releases on the demand schedule  """  
      self.ProcessTime:int = obj["ProcessTime"]
      """  Booktime of the related bookrel by the sales order releases on the demand schedule  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line Number to which this record is related.  """  
      self.QuoteRelNum:int = obj["QuoteRelNum"]
      """  The release number to which this schedule is related.  """  
      self.CTPNeedByDate:str = obj["CTPNeedByDate"]
      """  Date customer needs the item to be delivered and calculated by CTP  """  
      self.CTPShipDate:str = obj["CTPShipDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date and calculated by CTP.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.CTPManualConfirm:bool = obj["CTPManualConfirm"]
      """  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  """  
      self.CTPSource:str = obj["CTPSource"]
      """  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandSchedule.ShipToCustNum is  disabled  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      self.EDI_OTMFCountry:str = obj["EDI_OTMFCountry"]
      """  Support for OTMFCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTMFCountryNum will be populated based on it  """  
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.EnableLog:bool = obj["EnableLog"]
      """  Indicates if the Log action item is available.  """  
      self.EnableOverrideReject:bool = obj["EnableOverrideReject"]
      """  Indicates if the OverrideSystemReject option is available or not.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the user Reject option is available.  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.IUM:str = obj["IUM"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.PartNum:str = obj["PartNum"]
      self.PONum:str = obj["PONum"]
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.SalesUM:str = obj["SalesUM"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Contains the Ship To Address  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.DmdMassGrpCreatedBy:str = obj["DmdMassGrpCreatedBy"]
      self.MarkForNumInactive:bool = obj["MarkForNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildDisplayAddress_input:
   """ Required : 
   addressList
   """  
   def __init__(self, obj):
      self.addressList:str = obj["addressList"]
      pass

class BuildDisplayAddress_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ChangeCreateNewOrder_input:
   """ Required : 
   ipCreateNewSO
   ds
   """  
   def __init__(self, obj):
      self.ipCreateNewSO:bool = obj["ipCreateNewSO"]
      """  Boolean value to enable/disable CreateNewOrder flag  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeCreateNewOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailCustomerPrice_input:
   """ Required : 
   iCustomerPrice
   ds
   """  
   def __init__(self, obj):
      self.iCustomerPrice:int = obj["iCustomerPrice"]
      """  The Customer Price  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailCustomerPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailDemandContractLine_input:
   """ Required : 
   proposedDemandContractLine
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContractLine:int = obj["proposedDemandContractLine"]
      """  The proposed Demand Contract Line  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailDemandContractLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailInternalPrice_input:
   """ Required : 
   iInternalPrice
   ds
   """  
   def __init__(self, obj):
      self.iInternalPrice:int = obj["iInternalPrice"]
      """  The Internal Price  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailInternalPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailMktgCamp_input:
   """ Required : 
   iMktgCampaignID
   ds
   """  
   def __init__(self, obj):
      self.iMktgCampaignID:str = obj["iMktgCampaignID"]
      """  The Marketing Campaign ID  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailMktgCamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailPartNum_input:
   """ Required : 
   iPartNum
   ds
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  The part  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class ChangeDemandDetailPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPartNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeDemandDetailRevisionNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailUOM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailUnitPrice_input:
   """ Required : 
   iUnitPrice
   ds
   """  
   def __init__(self, obj):
      self.iUnitPrice:int = obj["iUnitPrice"]
      """  The Unit Price  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadBTCustID_input:
   """ Required : 
   proposedBTCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedBTCustID:str = obj["proposedBTCustID"]
      """  The proposed Bill To Cust ID  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadBTCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadCancelPO_input:
   """ Required : 
   ipCancelPO
   ds
   """  
   def __init__(self, obj):
      self.ipCancelPO:bool = obj["ipCancelPO"]
      """  Boolean value to enable/disable Cancel PO flag  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadCancelPO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadDemandContractNum_input:
   """ Required : 
   proposedDemandContractNum
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContractNum:int = obj["proposedDemandContractNum"]
      """  The proposed Demand Contract Number  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadDemandContractNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadDemandContract_input:
   """ Required : 
   proposedDemandContract
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContract:str = obj["proposedDemandContract"]
      """  The proposed Demand Contract  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadDemandContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadERSOrder_input:
   """ Required : 
   proposedERSOrder
   ds
   """  
   def __init__(self, obj):
      self.proposedERSOrder:bool = obj["proposedERSOrder"]
      """  The proposed ERS Order  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadERSOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipTo Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The proposed Ship To Num  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleCreateShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_DemandScheduleCreateTableset] = obj["ds"]
      pass

class ChangeDemandScheduleCreateShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCreateCycleList:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DemandScheduleCreateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleDeliveryDays_input:
   """ Required : 
   newDeliveryDays
   ds
   """  
   def __init__(self, obj):
      self.newDeliveryDays:int = obj["newDeliveryDays"]
      """  The new DeliveryDays  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleDeliveryDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleMFCustID_input:
   """ Required : 
   ipMFCustID
   ds
   """  
   def __init__(self, obj):
      self.ipMFCustID:str = obj["ipMFCustID"]
      """  The proposed Mark For Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleMFCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleMarkForNum_input:
   """ Required : 
   proposedMarkForNum
   ds
   """  
   def __init__(self, obj):
      self.proposedMarkForNum:str = obj["proposedMarkForNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleMarkForNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleNeedByDate_input:
   """ Required : 
   proposedNeedByDate
   ds
   """  
   def __init__(self, obj):
      self.proposedNeedByDate:str = obj["proposedNeedByDate"]
      """  The Proposed NeedByDate  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleNeedByDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleOTSDetails_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleOTSDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandSchedulePlant_input:
   """ Required : 
   proposedPlant
   ds
   """  
   def __init__(self, obj):
      self.proposedPlant:str = obj["proposedPlant"]
      """  The Proposed Plant  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandSchedulePlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleReqDate_input:
   """ Required : 
   proposedReqDate
   ds
   """  
   def __init__(self, obj):
      self.proposedReqDate:str = obj["proposedReqDate"]
      """  The Proposed ReqDate  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleReqDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleSellingReqQty_input:
   """ Required : 
   proposedSellingReqQty
   ds
   """  
   def __init__(self, obj):
      self.proposedSellingReqQty:int = obj["proposedSellingReqQty"]
      """  The proposed Selling Req Quantity  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleSellingReqQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipTo Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleUseOTMF_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleUseOTMF_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscAmount_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeMiscAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscCode_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscPercent_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class ChangeMiscPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPartRevisionChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class CheckPartRevisionChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.cConfigPartMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CloseAllSchedules_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      pass

class CloseAllSchedules_output:
   def __init__(self, obj):
      pass

class CloseDemandDetail_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Detail Sequence number  """  
      pass

class CloseDemandDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class CloseDemandHead_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      pass

class CloseDemandHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class CloseDemandSchedule_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      pass

class CloseDemandSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class ConfigurationChangePart_input:
   """ Required : 
   demandDtlSysRowID
   """  
   def __init__(self, obj):
      self.demandDtlSysRowID:str = obj["demandDtlSysRowID"]
      """  DemandDtl SysRowID  """  
      pass

class ConfigurationChangePart_output:
   def __init__(self, obj):
      pass

class ConfigurationRefreshQty_input:
   """ Required : 
   demandDetailSysRowID
   """  
   def __init__(self, obj):
      self.demandDetailSysRowID:str = obj["demandDetailSysRowID"]
      """  Demand Details SysRowID  """  
      pass

class ConfigurationRefreshQty_output:
   def __init__(self, obj):
      pass

class CreateDemandDetailFromContractLines_input:
   """ Required : 
   ds
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractDtlTableset] = obj["ds"]
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence  """  
      pass

class CreateDemandDetailFromContractLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   demandContractNum
   demandHeadSeq
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteScheduleByScheduleNumberKeepHeader_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   cScheduleNumber
   ds
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.cScheduleNumber:str = obj["cScheduleNumber"]
      """  Tje Schedule Number to delete  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class DeleteScheduleByScheduleNumberKeepHeader_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.cReturnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteScheduleByScheduleNumber_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   cScheduleNumber
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.cScheduleNumber:str = obj["cScheduleNumber"]
      """  The Schedule Number to delete  """  
      pass

class DeleteScheduleByScheduleNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cReturnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class EDIHeaderValidate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class EDIHeaderValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cReturnMessage:str = obj["parameters"]
      self.dprocess:bool = obj["dprocess"]
      self.matchDemand:bool = obj["matchDemand"]
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DemandContractDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations.  """  
      self.DocPriceTolerance:int = obj["DocPriceTolerance"]
      """  Defines the tolerance for price difference validations in document currency.  """  
      self.Rpt1PriceTolerance:int = obj["Rpt1PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt2PriceTolerance:int = obj["Rpt2PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt3PriceTolerance:int = obj["Rpt3PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandContractDtlTableset:
   def __init__(self, obj):
      self.DemandContractDtl:list[Erp_Tablesets_DemandContractDtlRow] = obj["DemandContractDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandDetail is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The contract line this demand line is for.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderDtl record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The OrderDtl record this demand detail is linked to.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other sales order detail records that have been created by this demand.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which the line item detail record is associated with. This is part of the foreign key to QuoteHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number to which this line was related. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.ScheduleType:str = obj["ScheduleType"]
      """  The schedule type from the trading partner.  Reference only.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandDetail has been rejected by the user.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record has been written to an OrderDtl.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the DemandDetail record is in a "open or closed" status.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand entry if the CRM module is installed.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Only used for audit purposes for EDI.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Only used for audit purposes for EDI.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Only used for audit purposes for EDI.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.EDIUnitPrice:int = obj["EDIUnitPrice"]
      """  The Incoming EDI Unit Price.  """  
      self.CumulativeQty:int = obj["CumulativeQty"]
      """  The total quantity that has been received according to the training partner data  """  
      self.CumulativeDate:str = obj["CumulativeDate"]
      """  The date when the trading partner calculated the cumulative quantity field  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  A qty that will create a new reconciliation adjustment.  """  
      self.StartCumDate:str = obj["StartCumDate"]
      """  The date since the trading partner has been accumulating the quantities.  """  
      self.LastShipmentID:int = obj["LastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.LastShipmentQty:int = obj["LastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.LastShipmentDate:str = obj["LastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.LastMasterPack:int = obj["LastMasterPack"]
      """  Last Master Pack ID  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Contains the internal system unit price in a foreign currency  """  
      self.DocEDIUnitPrice:int = obj["DocEDIUnitPrice"]
      """  Contains the Customer Price in a foreign currency  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """  This is the Internal Price assigned by the system calculated from the part sales price or a price list. It will be used when the Demand Contract is using Internal Pricing.  """  
      self.DocInternalPrice:int = obj["DocInternalPrice"]
      """  The doc currency value of the internal price  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.TPQuoteNum:int = obj["TPQuoteNum"]
      """  Trading Partner Quote Number. This is not an internal quote number, it is the quote sent by the trading partner.  """  
      self.TPQuoteLine:int = obj["TPQuoteLine"]
      """  Trading Partner Quote Line Number. This is not related to an internal quote, it is sent by the trading partner.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt1InternalPrice:int = obj["Rpt1InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt2InternalPrice:int = obj["Rpt2InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt3InternalPrice:int = obj["Rpt3InternalPrice"]
      """  Same as Internal Price except that this field contains the Internal Price in a report currency  """  
      self.Rpt1EDIUnitPrice:int = obj["Rpt1EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.Rpt2EDIUnitPrice:int = obj["Rpt2EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.Rpt3EDIUnitPrice:int = obj["Rpt3EDIUnitPrice"]
      """  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  """  
      self.BlockProcLine:bool = obj["BlockProcLine"]
      """  Indicates if current line is blocked for processing.  """  
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  This is field is similar to DemandContract. The field CUMMSetting helps to choose how the DemandReconciliation will open.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.EnableCreateSchedule:bool = obj["EnableCreateSchedule"]
      """  Indicates if the Create Demand Schedule option is available.  """  
      self.EnableDeleteReleases:bool = obj["EnableDeleteReleases"]
      self.EnableDeleteSchedule:bool = obj["EnableDeleteSchedule"]
      """  Indicates if the Delete Schedule by Schedule Number option is available.  """  
      self.EnableLog:bool = obj["EnableLog"]
      """  Indicates if the Log action item is available.  """  
      self.EnableOnlyPart:bool = obj["EnableOnlyPart"]
      """  This field is true is Demand Detail is posted or has link with SO.  """  
      self.EnableOverrideReject:bool = obj["EnableOverrideReject"]
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available.  """  
      self.EnableRevMatch:bool = obj["EnableRevMatch"]
      """  Indicates if the Review and Matching options are available.  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.MultipleXRef:bool = obj["MultipleXRef"]
      """  True when the XRefPartNum has multiple references.  """  
      self.PriceDiscrepancy:bool = obj["PriceDiscrepancy"]
      """  True when exists a Price Discrepancy beetwen UnitPrice and EDIUnitPrice  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.Configured:str = obj["Configured"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DemandContractDtlSalesUM:str = obj["DemandContractDtlSalesUM"]
      self.DemandContractHdrCUMMSetting:str = obj["DemandContractHdrCUMMSetting"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandDtlMatchingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.PartNum:str = obj["PartNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.DemandContract:str = obj["DemandContract"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.Rejected:bool = obj["Rejected"]
      """  Indicates if the user chose to reject this record.  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      self.IncludePOForReconcile:bool = obj["IncludePOForReconcile"]
      self.PONum:str = obj["PONum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandDtlReviewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.DemandContract:str = obj["DemandContract"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.MDPV:int = obj["MDPV"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.TotalQtyDifference:int = obj["TotalQtyDifference"]
      self.TotalCostQtyDifference:int = obj["TotalCostQtyDifference"]
      self.IncludePOForReconcile:bool = obj["IncludePOForReconcile"]
      self.PONum:str = obj["PONum"]
      self.ReviewUOM:str = obj["ReviewUOM"]
      """  Unit of Measure,  The Part Stocking UOM, if not valid part then DemandDtl.SalesUM  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandEntryTableset:
   def __init__(self, obj):
      self.DemandHead:list[Erp_Tablesets_DemandHeadRow] = obj["DemandHead"]
      self.DemandDetail:list[Erp_Tablesets_DemandDetailRow] = obj["DemandDetail"]
      self.DemandMiscChg:list[Erp_Tablesets_DemandMiscChgRow] = obj["DemandMiscChg"]
      self.DemandSchedule:list[Erp_Tablesets_DemandScheduleRow] = obj["DemandSchedule"]
      self.DemandMiscChgDH:list[Erp_Tablesets_DemandMiscChgDHRow] = obj["DemandMiscChgDH"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The OrderHed record this demand is linked to.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is a mandatory field used to enter the customers Purchase Order Number.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.AcceptType:str = obj["AcceptType"]
      """   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.Accepted:bool = obj["Accepted"]
      """  Indicates if this demand has been accepted or not.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandHead has been rejected by the user.  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI.  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  Do Not Process  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Flag at the Header Level that indicate that the demand can be process.  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  new orders will be created when it is set to true  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  Sales Order linked to this Demand  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.BatchNum:str = obj["BatchNum"]
      """  EDI Batch Control Number  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates if the One Time Shipto information is to be used.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.CustAddrList:str = obj["CustAddrList"]
      """  Holds a string with the customer address  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.BTCustID:str = obj["BTCustID"]
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BTAddressList:str = obj["BTAddressList"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.EnableGetLines:bool = obj["EnableGetLines"]
      """  Indicates if the Get Contract Lines option is available.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available  """  
      self.EnableProcess:bool = obj["EnableProcess"]
      """  Indicates if the Process action item is available.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.EnableLog:bool = obj["EnableLog"]
      self.DemandSchedAvail:bool = obj["DemandSchedAvail"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Indicates if the recently created order should be placed on hold. Defaults from Contract.  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Ship To Address List.  """  
      self.EDITran_Type:str = obj["EDITran_Type"]
      """  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  """  
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  """  
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  Country name  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      """  Description of the reservation priority. Example "High".  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsDescription:str = obj["TermsDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandHeadListTableset:
   def __init__(self, obj):
      self.DemandHeadList:list[Erp_Tablesets_DemandHeadListRow] = obj["DemandHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The OrderHed record this demand is linked to.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is a mandatory field used to enter the customers Purchase Order Number.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this line is being run in a test mode.  """  
      self.POType:str = obj["POType"]
      """  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  """  
      self.AcceptType:str = obj["AcceptType"]
      """   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.Accepted:bool = obj["Accepted"]
      """  Indicates if this demand has been accepted or not.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandHead has been rejected by the user.  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI.  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  Do Not Process  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Flag at the Header Level that indicate that the demand can be process.  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  new orders will be created when it is set to true  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  Sales Order linked to this Demand  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.BatchNum:str = obj["BatchNum"]
      """  EDI Batch Control Number  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  Ship the good by this time  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS ShipToNum  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates if the One Time Shipto information is to be used.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.EnableProcess:bool = obj["EnableProcess"]
      """  Indicates if the Process action item is available.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the Reject option is available  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  """  
      self.OpenContract:bool = obj["OpenContract"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Indicates if the recently created order should be placed on hold. Defaults from Contract.  """  
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  OTS Country Description  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  OTS Tax Region Description  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Ship To Address List.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BTAddressList:str = obj["BTAddressList"]
      self.BTCustID:str = obj["BTCustID"]
      self.CustAddrList:str = obj["CustAddrList"]
      """  Holds a string with the customer address  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandSchedAvail:bool = obj["DemandSchedAvail"]
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.EDITran_Type:str = obj["EDITran_Type"]
      """  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  """  
      self.EnableGetLines:bool = obj["EnableGetLines"]
      """  Indicates if the Get Contract Lines option is available.  """  
      self.EnableLog:bool = obj["EnableLog"]
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryDescription_:str = obj["OTSCountryDescription_"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMatchingTableset:
   def __init__(self, obj):
      self.DemandDtlMatching:list[Erp_Tablesets_DemandDtlMatchingRow] = obj["DemandDtlMatching"]
      self.OrderRelToMatch:list[Erp_Tablesets_OrderRelToMatchRow] = obj["OrderRelToMatch"]
      self.DemandScheduleToMatch:list[Erp_Tablesets_DemandScheduleToMatchRow] = obj["DemandScheduleToMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandMiscChgDHRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand misc charge is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The DemandHead this charge is for.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.Quoting:str = obj["Quoting"]
      """  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand misc charge is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The DemandHead this charge is for.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.Quoting:str = obj["Quoting"]
      """  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReviewTableset:
   def __init__(self, obj):
      self.DemandDtlReview:list[Erp_Tablesets_DemandDtlReviewRow] = obj["DemandDtlReview"]
      self.DemandSchedReview:list[Erp_Tablesets_DemandSchedReviewRow] = obj["DemandSchedReview"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandSchedReviewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.DemandReviewSeq:int = obj["DemandReviewSeq"]
      self.ReqDate:str = obj["ReqDate"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.CurDemandQty:int = obj["CurDemandQty"]
      self.CurBalance:int = obj["CurBalance"]
      self.ProposedDemandQty:int = obj["ProposedDemandQty"]
      self.ProposedBalance:int = obj["ProposedBalance"]
      self.DemandReference:str = obj["DemandReference"]
      self.QuantityDifference:int = obj["QuantityDifference"]
      self.BalanceDifference:int = obj["BalanceDifference"]
      self.CostQtyDifference:int = obj["CostQtyDifference"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleCreateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.PartNum:str = obj["PartNum"]
      self.BeginDate:str = obj["BeginDate"]
      self.EndDate:str = obj["EndDate"]
      self.DateType:str = obj["DateType"]
      self.QuantityPer:int = obj["QuantityPer"]
      self.CreateCycle:str = obj["CreateCycle"]
      self.CreateType:str = obj["CreateType"]
      self.DemandContract:str = obj["DemandContract"]
      """  The contract name  """  
      self.LineDesc:str = obj["LineDesc"]
      """  The description of the line the schedule is being created for.  """  
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.Plant:str = obj["Plant"]
      self.PlantName:str = obj["PlantName"]
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleCreateTableset:
   def __init__(self, obj):
      self.DemandScheduleCreate:list[Erp_Tablesets_DemandScheduleCreateRow] = obj["DemandScheduleCreate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand schedule is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The sequence from the DemandDetail record this DemandSchedule is related to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  """  
      self.GroupID:str = obj["GroupID"]
      """  All invoices belong to a group until the group is closed. The GroupID is assigned by the user.  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  """  
      self.MarkForNum:str = obj["MarkForNum"]
      """  The Mark For to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.DeliveryDays:int = obj["DeliveryDays"]
      """  The delivery days required for the shipment to reach its destination.  Defaults from Customer.DemandDeliveryDays or ShipTo.DemandDeliveryDays.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  """  
      self.DemandType:str = obj["DemandType"]
      """   The type of demand this line represents.  Values are:
InForecast - Incoming Forecast (Forecasts)
InUnfirm - Incoming Unfirm Releases (Unfirm OrderRel)
InShSched - Incoming Shipping Schedule (Firm OrderRel)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales order number of the OrderRel record this DemandSchedule is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number of the OrderRel record this DemandSchedule is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Sales order release number of the OrderRel record this DemandSchedule is linked to.  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  Indicates if the DemandSchedule has been rejected by the user.  """  
      self.RAN:str = obj["RAN"]
      """  RAN Number.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  """  
      self.DemandReference:str = obj["DemandReference"]
      """  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this record has been written to an OrderDtl.  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  Indicates if the DemandDetail has been rejected by the system.  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  Indicates if the system rejection should be overridden so the record can be accepted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OpenSchedule:bool = obj["OpenSchedule"]
      """  Indicates if this schedule is open.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.DocumentName:str = obj["DocumentName"]
      """  The document that initiated the demand.  Will be blank when the demand is manually entered.  """  
      self.ForecastEndDate:str = obj["ForecastEndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.Location:str = obj["Location"]
      """  The location within the customer shipto address.  For future use.  """  
      self.TransportID:str = obj["TransportID"]
      """  The code of the transport routing/time. For future use.  """  
      self.ShipbyTime:int = obj["ShipbyTime"]
      """  Ship the good by this time.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used.  """  
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
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.SubShipTo:str = obj["SubShipTo"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  """  
      self.ShipRouting:str = obj["ShipRouting"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Last update to the demand schedule record  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  Bookdate of the related bookrel by the sales order releases on the demand schedule  """  
      self.ProcessTime:int = obj["ProcessTime"]
      """  Booktime of the related bookrel by the sales order releases on the demand schedule  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number to which this record is related.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line Number to which this record is related.  """  
      self.QuoteRelNum:int = obj["QuoteRelNum"]
      """  The release number to which this schedule is related.  """  
      self.CTPNeedByDate:str = obj["CTPNeedByDate"]
      """  Date customer needs the item to be delivered and calculated by CTP  """  
      self.CTPShipDate:str = obj["CTPShipDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date and calculated by CTP.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.CTPManualConfirm:bool = obj["CTPManualConfirm"]
      """  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  """  
      self.CTPSource:str = obj["CTPSource"]
      """  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandSchedule.ShipToCustNum is  disabled  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      self.EDI_OTMFCountry:str = obj["EDI_OTMFCountry"]
      """  Support for OTMFCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTMFCountryNum will be populated based on it  """  
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      """  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  """  
      self.EnableLog:bool = obj["EnableLog"]
      """  Indicates if the Log action item is available.  """  
      self.EnableOverrideReject:bool = obj["EnableOverrideReject"]
      """  Indicates if the OverrideSystemReject option is available or not.  """  
      self.EnableReject:bool = obj["EnableReject"]
      """  Indicates if the user Reject option is available.  """  
      self.EnableUnreject:bool = obj["EnableUnreject"]
      self.IUM:str = obj["IUM"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OTSAllowed:bool = obj["OTSAllowed"]
      """  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  """  
      self.PartNum:str = obj["PartNum"]
      self.PONum:str = obj["PONum"]
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Indicates if this record is in read-only mode.  """  
      self.SalesUM:str = obj["SalesUM"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Contains the Ship To Address  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandContractHdrDemandContract:str = obj["DemandContractHdrDemandContract"]
      self.DmdMassGrpCreatedBy:str = obj["DmdMassGrpCreatedBy"]
      self.MarkForNumInactive:bool = obj["MarkForNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleToMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      self.ReqDate:str = obj["ReqDate"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.OurReqQty:int = obj["OurReqQty"]
      """  .  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.DemandReference:str = obj["DemandReference"]
      self.Rejected:bool = obj["Rejected"]
      """  Indicates if this record has been rejected by the user.  """  
      self.IsMatched:bool = obj["IsMatched"]
      """  Indicates if the Demand Schedule has been matched either by the system or by the user.  """  
      self.SalesUM:str = obj["SalesUM"]
      self.IUM:str = obj["IUM"]
      self.DemandType:str = obj["DemandType"]
      """  Same as DemandSchedule.DemandType  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderRelToMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.ReqDate:str = obj["ReqDate"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  .  """  
      self.DemandReference:str = obj["DemandReference"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.Matched:bool = obj["Matched"]
      self.SalesUM:str = obj["SalesUM"]
      self.IUM:str = obj["IUM"]
      self.DemandType:str = obj["DemandType"]
      """  Same as DemandSchedule.DemandType  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Same as OrderRel.OpenRelease  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDemandEntryTableset:
   def __init__(self, obj):
      self.DemandHead:list[Erp_Tablesets_DemandHeadRow] = obj["DemandHead"]
      self.DemandDetail:list[Erp_Tablesets_DemandDetailRow] = obj["DemandDetail"]
      self.DemandMiscChg:list[Erp_Tablesets_DemandMiscChgRow] = obj["DemandMiscChg"]
      self.DemandSchedule:list[Erp_Tablesets_DemandScheduleRow] = obj["DemandSchedule"]
      self.DemandMiscChgDH:list[Erp_Tablesets_DemandMiscChgDHRow] = obj["DemandMiscChgDH"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBasePartAndConfigType_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  DemandDtl sysrowid  """  
      pass

class GetBasePartAndConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBasePartForConfig_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  Order Number of the target Assembly  """  
      pass

class GetBasePartForConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   demandContractNum
   demandHeadSeq
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
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

class GetCreateCycleListValues_input:
   """ Required : 
   iCustNum
   cShipToNum
   """  
   def __init__(self, obj):
      self.iCustNum:int = obj["iCustNum"]
      self.cShipToNum:str = obj["cShipToNum"]
      pass

class GetCreateCycleListValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.CreateCycleList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDemandContractDtl_input:
   """ Required : 
   iDemandContractNum
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Contract Number to get the lines from  """  
      pass

class GetDemandContractDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractDtlTableset] = obj["returnObj"]
      pass

class GetDemandDtlReview_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence Number  """  
      pass

class GetDemandDtlReview_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandReviewTableset] = obj["returnObj"]
      pass

class GetDemandHeadData_input:
   """ Required : 
   whereClauseDemandHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandHead:str = obj["whereClauseDemandHead"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetDemandHeadData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetDemandMatching_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence Number  """  
      pass

class GetDemandMatching_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandMatchingTableset] = obj["returnObj"]
      pass

class GetDemandScheduleCreate_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence Number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Sequence Number  """  
      pass

class GetDemandScheduleCreate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandScheduleCreateTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cCreateCycleList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListCustomWithPaging_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListCustomWithPaging_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListCustom_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_DemandHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDemandDetail_input:
   """ Required : 
   ds
   demandContractNum
   demandHeadSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      pass

class GetNewDemandDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandHead_input:
   """ Required : 
   ds
   demandContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetNewDemandHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandMiscChgDH_input:
   """ Required : 
   ds
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandMiscChgDH_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandMiscChg_input:
   """ Required : 
   ds
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandMiscChg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandSchedule_input:
   """ Required : 
   ds
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPriceDiscrepancy_input:
   """ Required : 
   ipCustNum
   ipPONum
   ipUnitPrice
   ipEDIUnitPrice
   ipDemandDtlSeq
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  CustNum  """  
      self.ipPONum:str = obj["ipPONum"]
      """  poNum_ex  """  
      self.ipUnitPrice:int = obj["ipUnitPrice"]
      """  UnitPrice  """  
      self.ipEDIUnitPrice:int = obj["ipEDIUnitPrice"]
      """  EDIUnitPrice  """  
      self.ipDemandDtlSeq:int = obj["ipDemandDtlSeq"]
      """  DemandDtlSeq  """  
      pass

class GetPriceDiscrepancy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPriceDiscrepancy:bool = obj["opPriceDiscrepancy"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDemandHead
   whereClauseDemandDetail
   whereClauseDemandMiscChg
   whereClauseDemandSchedule
   whereClauseDemandMiscChgDH
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandHead:str = obj["whereClauseDemandHead"]
      self.whereClauseDemandDetail:str = obj["whereClauseDemandDetail"]
      self.whereClauseDemandMiscChg:str = obj["whereClauseDemandMiscChg"]
      self.whereClauseDemandSchedule:str = obj["whereClauseDemandSchedule"]
      self.whereClauseDemandMiscChgDH:str = obj["whereClauseDemandMiscChgDH"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
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

class MassCreateDemandSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandScheduleCreateTableset] = obj["ds"]
      pass

class MassCreateDemandSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandScheduleCreateTableset] = obj["ds"]
      self.cReturnText:str = obj["parameters"]
      pass

      """  output parameters  """  

class OpenDemandDetail_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Detail Sequence number  """  
      pass

class OpenDemandDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class OpenDemandHeadKeepDemandDetail_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   ds
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class OpenDemandHeadKeepDemandDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OpenDemandHead_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      pass

class OpenDemandHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class OpenDemandSchedule_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      pass

class OpenDemandSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class PartValidation_input:
   """ Required : 
   iContractNum
   iHeadSeq
   iDocName
   iPartNum
   iXPartNum
   """  
   def __init__(self, obj):
      self.iContractNum:int = obj["iContractNum"]
      self.iHeadSeq:int = obj["iHeadSeq"]
      self.iDocName:str = obj["iDocName"]
      self.iPartNum:str = obj["iPartNum"]
      self.iXPartNum:str = obj["iXPartNum"]
      pass

class PartValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPartNum:str = obj["parameters"]
      self.oValidPart:bool = obj["oValidPart"]
      self.oPartDesc:str = obj["parameters"]
      self.oUOM:str = obj["parameters"]
      self.oXRefPartType:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessDemand_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence Number  """  
      pass

class ProcessDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cReturnMessage:str = obj["parameters"]
      self.cRejectFlag:bool = obj["cRejectFlag"]
      pass

      """  output parameters  """  

class ProcessMatching_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandMatchingTableset] = obj["ds"]
      pass

class ProcessMatching_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMatchingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RejectDemandDetail_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Detail Sequence number  """  
      pass

class RejectDemandDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class RejectDemandHead_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      pass

class RejectDemandHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class RejectDemandScheduleKeepSchedules_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   ds
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class RejectDemandScheduleKeepSchedules_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RejectDemandSchedule_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      pass

class RejectDemandSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class SetReadyToProcess_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   lReady
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence Number  """  
      self.lReady:bool = obj["lReady"]
      """  Indicates if the demand is ready to be processed  """  
      pass

class SetReadyToProcess_output:
   def __init__(self, obj):
      pass

class UnlockDemand_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Detail Sequence number  """  
      pass

class UnlockDemand_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class UnrejectDemandDetail_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Detail Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Detail Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Detail Detail Sequence number  """  
      pass

class UnrejectDemandDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class UnrejectDemandHead_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Header Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Header Sequence number  """  
      pass

class UnrejectDemandHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class UnrejectDemandScheduleKeepSchedules_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   ds
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class UnrejectDemandScheduleKeepSchedules_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnrejectDemandSchedule_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iDemandScheduleSeq
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Schedule Contract Num  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Schedule Header Sequence number  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The Demand Schedule Detail Sequence number  """  
      self.iDemandScheduleSeq:int = obj["iDemandScheduleSeq"]
      """  The Demand Schedule Sequence number  """  
      pass

class UnrejectDemandSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandEntryTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandEntryTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

