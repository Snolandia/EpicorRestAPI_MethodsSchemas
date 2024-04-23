import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IDNumbersSvc
# Description: Service for creating ID Number formats
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IDNumbers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IDNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IDNumbers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IDNumCnfgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers",headers=creds) as resp:
           return await resp.json()

async def post_IDNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IDNumbers_Company_FormatID(Company, FormatID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IDNumber item
   Description: Calls GetByID to retrieve the IDNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IDNumCnfgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers(" + Company + "," + FormatID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IDNumbers_Company_FormatID(Company, FormatID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IDNumber for the service
   Description: Calls UpdateExt to update IDNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers(" + Company + "," + FormatID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IDNumbers_Company_FormatID(Company, FormatID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IDNumber item
   Description: Call UpdateExt to delete IDNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers(" + Company + "," + FormatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_IDNumbers_Company_FormatID_IDNumCnfgSeqs(Company, FormatID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get IDNumCnfgSeqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_IDNumCnfgSeqs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IDNumCnfgSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers(" + Company + "," + FormatID + ")/IDNumCnfgSeqs",headers=creds) as resp:
           return await resp.json()

async def get_IDNumbers_Company_FormatID_IDNumCnfgSeqs_Company_FormatID_DefaultPrefix_TransYear_StartSequence(Company, FormatID, DefaultPrefix, TransYear, StartSequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IDNumCnfgSeq item
   Description: Calls GetByID to retrieve the IDNumCnfgSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IDNumCnfgSeq1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IDNumCnfgSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumbers(" + Company + "," + FormatID + ")/IDNumCnfgSeqs(" + Company + "," + FormatID + "," + DefaultPrefix + "," + TransYear + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_IDNumCnfgSeqs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IDNumCnfgSeqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IDNumCnfgSeqs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IDNumCnfgSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumCnfgSeqs",headers=creds) as resp:
           return await resp.json()

async def post_IDNumCnfgSeqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IDNumCnfgSeqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgSeqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgSeqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumCnfgSeqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IDNumCnfgSeqs_Company_FormatID_DefaultPrefix_TransYear_StartSequence(Company, FormatID, DefaultPrefix, TransYear, StartSequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IDNumCnfgSeq item
   Description: Calls GetByID to retrieve the IDNumCnfgSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IDNumCnfgSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IDNumCnfgSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumCnfgSeqs(" + Company + "," + FormatID + "," + DefaultPrefix + "," + TransYear + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IDNumCnfgSeqs_Company_FormatID_DefaultPrefix_TransYear_StartSequence(Company, FormatID, DefaultPrefix, TransYear, StartSequence, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IDNumCnfgSeq for the service
   Description: Calls UpdateExt to update IDNumCnfgSeq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IDNumCnfgSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IDNumCnfgSeqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumCnfgSeqs(" + Company + "," + FormatID + "," + DefaultPrefix + "," + TransYear + "," + StartSequence + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IDNumCnfgSeqs_Company_FormatID_DefaultPrefix_TransYear_StartSequence(Company, FormatID, DefaultPrefix, TransYear, StartSequence, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IDNumCnfgSeq item
   Description: Call UpdateExt to delete IDNumCnfgSeq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IDNumCnfgSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/IDNumCnfgSeqs(" + Company + "," + FormatID + "," + DefaultPrefix + "," + TransYear + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_AvailableIDNumFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AvailableIDNumFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailableIDNumFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailableIDNumFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/AvailableIDNumFormats",headers=creds) as resp:
           return await resp.json()

async def post_AvailableIDNumFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailableIDNumFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailableIDNumFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailableIDNumFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/AvailableIDNumFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AvailableIDNumFormats_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AvailableIDNumFormat item
   Description: Calls GetByID to retrieve the AvailableIDNumFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailableIDNumFormat
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailableIDNumFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/AvailableIDNumFormats(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AvailableIDNumFormats_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AvailableIDNumFormat for the service
   Description: Calls UpdateExt to update AvailableIDNumFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailableIDNumFormat
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailableIDNumFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/AvailableIDNumFormats(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AvailableIDNumFormats_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AvailableIDNumFormat item
   Description: Call UpdateExt to delete AvailableIDNumFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailableIDNumFormat
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/AvailableIDNumFormats(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IDNumCnfgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIDNumCnfg, whereClauseIDNumCnfgSeq, whereClauseAvailableIDNumFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseIDNumCnfg=" + whereClauseIDNumCnfg
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIDNumCnfgSeq=" + whereClauseIDNumCnfgSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAvailableIDNumFormat=" + whereClauseAvailableIDNumFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(formatID, epicorHeaders = None):
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
   params += "formatID=" + formatID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableFormatElements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableFormatElements
   Description: Load all Elements available for the ID Number format.
<param name="idType">idType</param>
   OperationID: GetAvailableFormatElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableFormatElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFormatElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfGenerationType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfGenerationType
   Description: This method should be called if the Generation Type changes.
   OperationID: OnChangeOfGenerationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfGenerationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfGenerationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfIDType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfIDType
   Description: This method should be called if the ID Type changes.
   OperationID: OnChangeOfIDType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfIDType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfIDType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNumberOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNumberOption
   Description: This method should be called if the number Option changes.
   OperationID: OnChangeNumberOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNumberOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNumberOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateIDNumberFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateIDNumberFormat
   Description: Generate ID Number Format
   OperationID: GenerateIDNumberFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateIDNumberFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateIDNumberFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetPreviousSeqLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetPreviousSeqLength
   Description: Set Previous SeqLength
   OperationID: SetPreviousSeqLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetPreviousSeqLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPreviousSeqLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIDNumCnfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIDNumCnfg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIDNumCnfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIDNumCnfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIDNumCnfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIDNumCnfgSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIDNumCnfgSeq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIDNumCnfgSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIDNumCnfgSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIDNumCnfgSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IDNumbersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableIDNumFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AvailableIDNumFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IDNumCnfgListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IDNumCnfgListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IDNumCnfgRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IDNumCnfgRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IDNumCnfgSeqRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IDNumCnfgSeqRow] = obj["value"]
      pass

class Erp_Tablesets_AvailableIDNumFormatRow:
   def __init__(self, obj):
      self.ElementCode:str = obj["ElementCode"]
      self.ElementDesc:str = obj["ElementDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description of Identification Number format.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.AddLeadingZeroDay:bool = obj["AddLeadingZeroDay"]
      """  Defines if Day is displayed with leading zeros or not.  """  
      self.AddLeadingZeroMonth:bool = obj["AddLeadingZeroMonth"]
      """  Defines if Month is displayed with leading zeros or not.  """  
      self.ConditionalSeparator:str = obj["ConditionalSeparator"]
      """  Separator is single character defined by user. It can be also used as Alternative Separator Character.  """  
      self.CountryCode:str = obj["CountryCode"]
      """  Country Code  """  
      self.Description:str = obj["Description"]
      """  Description of Identification Number format.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.FreeText1:str = obj["FreeText1"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.FreeText2:str = obj["FreeText2"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.Format:str = obj["Format"]
      """  Stores the format defined to generate the Identification Number.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.ManufacturerCode:str = obj["ManufacturerCode"]
      """  Manufacturer code specific to industry.  """  
      self.ModelYear:int = obj["ModelYear"]
      """  Model year for manufactured good.  Example may be October 2018 but the model year is actually 2019.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Specifies how numbers are generated for the identification number method. The number options are: Sequence system generated, Sequence entered manually, Full number entered.  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.StartMonth:int = obj["StartMonth"]
      """  The month when the year begins, starts the sequence over.  """  
      self.YearFormat:str = obj["YearFormat"]
      """  Defines whether the Year is displayed with 4, 2 or 1 digits .  """  
      self.IDType:str = obj["IDType"]
      """  Industry standard type such as HIN, VIN.  This will be used to default the format elements and used for validation.  """  
      self.WorldManufacturerCode:str = obj["WorldManufacturerCode"]
      """  World manufacturer code specific to industry.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IDNumberSample:str = obj["IDNumberSample"]
      self.FullNumAvail:bool = obj["FullNumAvail"]
      """  Flag to determine when the manual number option Full number entered is available to use.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
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
class DeleteByID_input:
   """ Required : 
   formatID
   """  
   def __init__(self, obj):
      self.formatID:str = obj["formatID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AvailableIDNumFormatRow:
   def __init__(self, obj):
      self.ElementCode:str = obj["ElementCode"]
      self.ElementDesc:str = obj["ElementDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description of Identification Number format.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgListTableset:
   def __init__(self, obj):
      self.IDNumCnfgList:list[Erp_Tablesets_IDNumCnfgListRow] = obj["IDNumCnfgList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IDNumCnfgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.AddLeadingZeroDay:bool = obj["AddLeadingZeroDay"]
      """  Defines if Day is displayed with leading zeros or not.  """  
      self.AddLeadingZeroMonth:bool = obj["AddLeadingZeroMonth"]
      """  Defines if Month is displayed with leading zeros or not.  """  
      self.ConditionalSeparator:str = obj["ConditionalSeparator"]
      """  Separator is single character defined by user. It can be also used as Alternative Separator Character.  """  
      self.CountryCode:str = obj["CountryCode"]
      """  Country Code  """  
      self.Description:str = obj["Description"]
      """  Description of Identification Number format.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.FreeText1:str = obj["FreeText1"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.FreeText2:str = obj["FreeText2"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.Format:str = obj["Format"]
      """  Stores the format defined to generate the Identification Number.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.ManufacturerCode:str = obj["ManufacturerCode"]
      """  Manufacturer code specific to industry.  """  
      self.ModelYear:int = obj["ModelYear"]
      """  Model year for manufactured good.  Example may be October 2018 but the model year is actually 2019.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Specifies how numbers are generated for the identification number method. The number options are: Sequence system generated, Sequence entered manually, Full number entered.  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.StartMonth:int = obj["StartMonth"]
      """  The month when the year begins, starts the sequence over.  """  
      self.YearFormat:str = obj["YearFormat"]
      """  Defines whether the Year is displayed with 4, 2 or 1 digits .  """  
      self.IDType:str = obj["IDType"]
      """  Industry standard type such as HIN, VIN.  This will be used to default the format elements and used for validation.  """  
      self.WorldManufacturerCode:str = obj["WorldManufacturerCode"]
      """  World manufacturer code specific to industry.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IDNumberSample:str = obj["IDNumberSample"]
      self.FullNumAvail:bool = obj["FullNumAvail"]
      """  Flag to determine when the manual number option Full number entered is available to use.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FormatID:str = obj["FormatID"]
      """  The Identification Number format identifier.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Default Prefix  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the format is Active. If not Active system will no longer allow it to be used.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IDNumCnfgTableset:
   def __init__(self, obj):
      self.IDNumCnfg:list[Erp_Tablesets_IDNumCnfgRow] = obj["IDNumCnfg"]
      self.IDNumCnfgSeq:list[Erp_Tablesets_IDNumCnfgSeqRow] = obj["IDNumCnfgSeq"]
      self.AvailableIDNumFormat:list[Erp_Tablesets_AvailableIDNumFormatRow] = obj["AvailableIDNumFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtIDNumCnfgTableset:
   def __init__(self, obj):
      self.IDNumCnfg:list[Erp_Tablesets_IDNumCnfgRow] = obj["IDNumCnfg"]
      self.IDNumCnfgSeq:list[Erp_Tablesets_IDNumCnfgSeqRow] = obj["IDNumCnfgSeq"]
      self.AvailableIDNumFormat:list[Erp_Tablesets_AvailableIDNumFormatRow] = obj["AvailableIDNumFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateIDNumberFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class GenerateIDNumberFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailableFormatElements_input:
   """ Required : 
   idType
   """  
   def __init__(self, obj):
      self.idType:str = obj["idType"]
      pass

class GetAvailableFormatElements_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IDNumCnfgTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   formatID
   """  
   def __init__(self, obj):
      self.formatID:str = obj["formatID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IDNumCnfgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IDNumCnfgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IDNumCnfgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IDNumCnfgListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIDNumCnfgSeq_input:
   """ Required : 
   ds
   formatID
   defaultPrefix
   transYear
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      self.formatID:str = obj["formatID"]
      self.defaultPrefix:str = obj["defaultPrefix"]
      self.transYear:int = obj["transYear"]
      pass

class GetNewIDNumCnfgSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIDNumCnfg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class GetNewIDNumCnfg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIDNumCnfg
   whereClauseIDNumCnfgSeq
   whereClauseAvailableIDNumFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIDNumCnfg:str = obj["whereClauseIDNumCnfg"]
      self.whereClauseIDNumCnfgSeq:str = obj["whereClauseIDNumCnfgSeq"]
      self.whereClauseAvailableIDNumFormat:str = obj["whereClauseAvailableIDNumFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IDNumCnfgTableset] = obj["returnObj"]
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

class OnChangeNumberOption_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class OnChangeNumberOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfGenerationType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfGenerationType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfIDType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfIDType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetPreviousSeqLength_input:
   """ Required : 
   ds
   previousSeqLength
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      self.previousSeqLength:int = obj["previousSeqLength"]
      pass

class SetPreviousSeqLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIDNumCnfgTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIDNumCnfgTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IDNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

