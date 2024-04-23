import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AssetDispEntrySvc
# Description: FA disposal entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AssetDispEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetDispEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries",headers=creds) as resp:
           return await resp.json()

async def post_AssetDispEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetDispEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries_Company_AssetNum_DisposalNum(Company, AssetNum, DisposalNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AssetDispEntry item
   Description: Calls GetByID to retrieve the AssetDispEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetDispEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AssetDispEntries_Company_AssetNum_DisposalNum(Company, AssetNum, DisposalNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AssetDispEntry for the service
   Description: Calls UpdateExt to update AssetDispEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetDispEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AssetDispEntries_Company_AssetNum_DisposalNum(Company, AssetNum, DisposalNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AssetDispEntry item
   Description: Call UpdateExt to delete AssetDispEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetDispEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries_Company_AssetNum_DisposalNum_FADispRegs(Company, AssetNum, DisposalNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FADispRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FADispRegs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADispRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADispRegs",headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries_Company_AssetNum_DisposalNum_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company, AssetNum, DisposalNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FADispReg item
   Description: Calls GetByID to retrieve the FADispReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADispReg1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries_Company_AssetNum_DisposalNum_FADisposalAttches(Company, AssetNum, DisposalNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FADisposalAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FADisposalAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADisposalAttches",headers=creds) as resp:
           return await resp.json()

async def get_AssetDispEntries_Company_AssetNum_DisposalNum_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company, AssetNum, DisposalNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FADisposalAttch item
   Description: Calls GetByID to retrieve the FADisposalAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADisposalAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FADispRegs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FADispRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FADispRegs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADispRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs",headers=creds) as resp:
           return await resp.json()

async def post_FADispRegs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FADispRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company, AssetNum, DisposalNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FADispReg item
   Description: Calls GetByID to retrieve the FADispReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADispReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company, AssetNum, DisposalNum, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FADispReg for the service
   Description: Calls UpdateExt to update FADispReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FADispReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company, AssetNum, DisposalNum, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FADispReg item
   Description: Call UpdateExt to delete FADispReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FADispReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FADisposalAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FADisposalAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FADisposalAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches",headers=creds) as resp:
           return await resp.json()

async def post_FADisposalAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FADisposalAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company, AssetNum, DisposalNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FADisposalAttch item
   Description: Calls GetByID to retrieve the FADisposalAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADisposalAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company, AssetNum, DisposalNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FADisposalAttch for the service
   Description: Calls UpdateExt to update FADisposalAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FADisposalAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company, AssetNum, DisposalNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FADisposalAttch item
   Description: Call UpdateExt to delete FADisposalAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FADisposalAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DisposalNum: Desc: DisposalNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFADisposal, whereClauseFADisposalAttch, whereClauseFADispReg, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFADisposal=" + whereClauseFADisposal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFADisposalAttch=" + whereClauseFADisposalAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFADispReg=" + whereClauseFADispReg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, disposalNum, epicorHeaders = None):
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "disposalNum=" + disposalNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDeprCalculated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDeprCalculated
   Description: Checks whether depreciation schedule was calculated for Fiscal Period of Disposal date
   OperationID: CheckDeprCalculated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDeprCalculated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDeprCalculated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveCustID
   Description: To be called on leave of custid field
   OperationID: LeaveCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveDisposalCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveDisposalCost
   Description: To be called on leave of DisposalCost field
   OperationID: LeaveDisposalCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposalCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposalCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveDisposalType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveDisposalType
   Description: To be called on leave of DisposalType field
   OperationID: LeaveDisposalType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposalType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposalType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveDisposed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveDisposed
   Description: To be called on leave of Disposed field
   OperationID: LeaveDisposed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveJobNum
   OperationID: LeaveJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveOrderNum
   Description: To be called on leave of ordernum field
   OperationID: LeaveOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeavePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeavePartNum
   Description: To be called on leave of partnum field
   OperationID: LeavePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveProceed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveProceed
   Description: To be called on leave of Proceed field
   OperationID: LeaveProceed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveProceed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveProceed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveWarehouseCode
   Description: To be called on leave of WarehouseCode field
   OperationID: LeaveWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveBinNum
   Description: To be called on leave of Bin field
   OperationID: LeaveBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetDepRecalcNeeded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetDepRecalcNeeded
   Description: Check if the asset or any of its registers requires depreciation calculation
   OperationID: CheckAssetDepRecalcNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetDepRecalcNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetDepRecalcNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnSetReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnSetReadyToPost
   Description: To be called on leave of ReadyToPost field with value 'true'
   OperationID: OnSetReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSetReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSetReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:  sets up the parameters for invoking the Serial Number Selection form
Notes:
<param name="ds">Asset Disposal DataSet</param><returns>The SelectSerialNumbersParams dataset</returns>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number scanned in the serial number selection form is valid for this transaction
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for FAdisposal record and
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFADisposal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFADisposal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADisposal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADisposal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADisposal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFADisposalAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFADisposalAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADisposalAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADisposalAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADisposalAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFADispReg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFADispReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADispReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADispReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADispReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FADispRegRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FADisposalAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FADisposalListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FADisposalRow] = obj["value"]
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

class Erp_Tablesets_FADispRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.PrevDepreciation:int = obj["PrevDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years.  """  
      self.CurrDepreciation:int = obj["CurrDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of current year.  """  
      self.BookValue:int = obj["BookValue"]
      """  The Book Value of a disposal is calculated as the disposal cost minus disposal depreciation minus disposal current year depreciation.  """  
      self.DocPrevDepreciation:int = obj["DocPrevDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years in the specified currency.  """  
      self.DocCurrDepreciation:int = obj["DocCurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  This is the Book Value of a disposal in the specified currency.  """  
      self.Rpt1PrevDepreciation:int = obj["Rpt1PrevDepreciation"]
      """  Reporting currency of the previous years disposal depreciation.  """  
      self.Rpt1CurrDepreciation:int = obj["Rpt1CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.Rpt2PrevDepreciation:int = obj["Rpt2PrevDepreciation"]
      """  Reporting currency value of the previous years disposal depreciation.  """  
      self.Rpt2CurrDepreciation:int = obj["Rpt2CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.Rpt3PrevDepreciation:int = obj["Rpt3PrevDepreciation"]
      """  Reporting currency value of the previous years disposal depreciation.  """  
      self.Rpt3CurrDepreciation:int = obj["Rpt3CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.PrevGrantDep:int = obj["PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.CurrGrantDep:int = obj["CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.DocPrevGrantDep:int = obj["DocPrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.DocCurrGrantDep:int = obj["DocCurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt1PrevGrantDep:int = obj["Rpt1PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt1CurrGrantDep:int = obj["Rpt1CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt2PrevGrantDep:int = obj["Rpt2PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt2CurrGrantDep:int = obj["Rpt2CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt3PrevGrantDep:int = obj["Rpt3PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt3CurrGrantDep:int = obj["Rpt3CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on disposal setting of the asset, that was used to create the disposal.  """  
      self.CurrCode:str = obj["CurrCode"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.DisposalProfitLoss:int = obj["DisposalProfitLoss"]
      """  Disposal Profit/Loss in base currency. Calculated field.  """  
      self.DocDisposalProfitLoss:int = obj["DocDisposalProfitLoss"]
      """  Disposal Profit/Loss in document currency. Calculated field.  """  
      self.Rpt1DisposalProfitLoss:int = obj["Rpt1DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt1 currency. Calculated field.  """  
      self.Rpt2DisposalProfitLoss:int = obj["Rpt2DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt2 currency. Calculated field.  """  
      self.Rpt3DisposalProfitLoss:int = obj["Rpt3DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt3 currency. Calculated field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FADisposalAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.DisposalNum:int = obj["DisposalNum"]
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

class Erp_Tablesets_FADisposalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.Disposed:str = obj["Disposed"]
      """  The date of Disposal.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the disposal.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  Internal customer number.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line of the customer invoice.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The orignal manufacturer of the disposal.  """  
      self.Model:str = obj["Model"]
      """  The model number of the disposal.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the disposal.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the disposal is posted to the gL.  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date of the posting to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user that posted the disposal to the GL.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the disposal is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number to which the disposal is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year in which the disposal is posted.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period in which the disposal is posted.  """  
      self.CustName:str = obj["CustName"]
      """  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order that is used to sell the disposal.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that built the disposal.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  flag to indicate that the disposal is allowed to be posted.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.DisposalType:str = obj["DisposalType"]
      """  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this disposal transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of the transferred asset to stock.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      self.PartLotTracked:bool = obj["PartLotTracked"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.WhseDescription:str = obj["WhseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FADisposalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.Disposed:str = obj["Disposed"]
      """  The date of Disposal.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the disposal.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  Internal customer number.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line of the customer invoice.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The orignal manufacturer of the disposal.  """  
      self.Model:str = obj["Model"]
      """  The model number of the disposal.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the disposal.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the disposal is posted to the gL.  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date of the posting to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user that posted the disposal to the GL.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the disposal is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number to which the disposal is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year in which the disposal is posted.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period in which the disposal is posted.  """  
      self.CustName:str = obj["CustName"]
      """  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order that is used to sell the disposal.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that built the disposal.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  flag to indicate that the disposal is allowed to be posted.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.DisposalType:str = obj["DisposalType"]
      """  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this disposal transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of the transferred asset to stock.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.TransferBVFrom:str = obj["TransferBVFrom"]
      """  Determines Asset Register from which Book Value will be taken as Proceeds.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CustID:str = obj["CustID"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether the serial numbers are required in AssetDispEntry  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.PartLotTracked:bool = obj["PartLotTracked"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      self.WhseDescription:str = obj["WhseDescription"]
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
class CheckAssetDepRecalcNeeded_input:
   """ Required : 
   assetNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      pass

class CheckAssetDepRecalcNeeded_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if depreciation calculation is required  """  
      pass

class CheckAssetTransactions_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class CheckAssetTransactions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: an empty string  """  
      pass

class CheckDeprCalculated_input:
   """ Required : 
   assetNum
   disposed
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.disposed:str = obj["disposed"]
      """  Disposal date  """  
      pass

class CheckDeprCalculated_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if Depreciation was calculated, false - otherwise  """  
      pass

   def parameters(self, obj):
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearReadyToPost_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class ClearReadyToPost_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   assetNum
   disposalNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.disposalNum:int = obj["disposalNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AssetDispEntryTableset:
   def __init__(self, obj):
      self.FADisposal:list[Erp_Tablesets_FADisposalRow] = obj["FADisposal"]
      self.FADisposalAttch:list[Erp_Tablesets_FADisposalAttchRow] = obj["FADisposalAttch"]
      self.FADispReg:list[Erp_Tablesets_FADispRegRow] = obj["FADispReg"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FADispRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.PrevDepreciation:int = obj["PrevDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years.  """  
      self.CurrDepreciation:int = obj["CurrDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of current year.  """  
      self.BookValue:int = obj["BookValue"]
      """  The Book Value of a disposal is calculated as the disposal cost minus disposal depreciation minus disposal current year depreciation.  """  
      self.DocPrevDepreciation:int = obj["DocPrevDepreciation"]
      """  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years in the specified currency.  """  
      self.DocCurrDepreciation:int = obj["DocCurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  This is the Book Value of a disposal in the specified currency.  """  
      self.Rpt1PrevDepreciation:int = obj["Rpt1PrevDepreciation"]
      """  Reporting currency of the previous years disposal depreciation.  """  
      self.Rpt1CurrDepreciation:int = obj["Rpt1CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.Rpt2PrevDepreciation:int = obj["Rpt2PrevDepreciation"]
      """  Reporting currency value of the previous years disposal depreciation.  """  
      self.Rpt2CurrDepreciation:int = obj["Rpt2CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.Rpt3PrevDepreciation:int = obj["Rpt3PrevDepreciation"]
      """  Reporting currency value of the previous years disposal depreciation.  """  
      self.Rpt3CurrDepreciation:int = obj["Rpt3CurrDepreciation"]
      """  Reporting currency value of the current year disposal depreciation.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  Reporting currency value of the disposal book value.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.PrevGrantDep:int = obj["PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.CurrGrantDep:int = obj["CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.DocPrevGrantDep:int = obj["DocPrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.DocCurrGrantDep:int = obj["DocCurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt1PrevGrantDep:int = obj["Rpt1PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt1CurrGrantDep:int = obj["Rpt1CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt2PrevGrantDep:int = obj["Rpt2PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt2CurrGrantDep:int = obj["Rpt2CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  """  
      self.Rpt3PrevGrantDep:int = obj["Rpt3PrevGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for previous years.  """  
      self.Rpt3CurrGrantDep:int = obj["Rpt3CurrGrantDep"]
      """  The disposed portion of the total Grant Depreciation already posted for the current year.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on disposal setting of the asset, that was used to create the disposal.  """  
      self.CurrCode:str = obj["CurrCode"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.DisposalProfitLoss:int = obj["DisposalProfitLoss"]
      """  Disposal Profit/Loss in base currency. Calculated field.  """  
      self.DocDisposalProfitLoss:int = obj["DocDisposalProfitLoss"]
      """  Disposal Profit/Loss in document currency. Calculated field.  """  
      self.Rpt1DisposalProfitLoss:int = obj["Rpt1DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt1 currency. Calculated field.  """  
      self.Rpt2DisposalProfitLoss:int = obj["Rpt2DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt2 currency. Calculated field.  """  
      self.Rpt3DisposalProfitLoss:int = obj["Rpt3DisposalProfitLoss"]
      """  Disposal Profit/Loss in Rpt3 currency. Calculated field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FADisposalAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.DisposalNum:int = obj["DisposalNum"]
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

class Erp_Tablesets_FADisposalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.Disposed:str = obj["Disposed"]
      """  The date of Disposal.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the disposal.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  Internal customer number.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line of the customer invoice.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The orignal manufacturer of the disposal.  """  
      self.Model:str = obj["Model"]
      """  The model number of the disposal.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the disposal.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the disposal is posted to the gL.  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date of the posting to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user that posted the disposal to the GL.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the disposal is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number to which the disposal is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year in which the disposal is posted.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period in which the disposal is posted.  """  
      self.CustName:str = obj["CustName"]
      """  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order that is used to sell the disposal.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that built the disposal.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  flag to indicate that the disposal is allowed to be posted.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.DisposalType:str = obj["DisposalType"]
      """  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this disposal transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of the transferred asset to stock.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      self.PartLotTracked:bool = obj["PartLotTracked"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.WhseDescription:str = obj["WhseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FADisposalListTableset:
   def __init__(self, obj):
      self.FADisposalList:list[Erp_Tablesets_FADisposalListRow] = obj["FADisposalList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FADisposalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Disposal.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Disposal.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal of an asset.  """  
      self.Disposed:str = obj["Disposed"]
      """  The date of Disposal.  """  
      self.DisposalCost:int = obj["DisposalCost"]
      """  The cost disposed from the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the disposal.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number of the customer.  """  
      self.CustNum:int = obj["CustNum"]
      """  Internal customer number.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line of the customer invoice.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The orignal manufacturer of the disposal.  """  
      self.Model:str = obj["Model"]
      """  The model number of the disposal.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the disposal.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the disposal is posted to the gL.  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date of the posting to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user that posted the disposal to the GL.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the disposal is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number to which the disposal is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year in which the disposal is posted.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period in which the disposal is posted.  """  
      self.CustName:str = obj["CustName"]
      """  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order that is used to sell the disposal.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that built the disposal.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  flag to indicate that the disposal is allowed to be posted.  """  
      self.Proceed:int = obj["Proceed"]
      """  The sales amount of the disposal.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.DisposalType:str = obj["DisposalType"]
      """  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this disposal transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of the transferred asset to stock.  """  
      self.DocDisposalCost:int = obj["DocDisposalCost"]
      """  The cost disposed from the asset in the currency specified.  """  
      self.Rpt1DisposalCost:int = obj["Rpt1DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt2DisposalCost:int = obj["Rpt2DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.Rpt3DisposalCost:int = obj["Rpt3DisposalCost"]
      """  Reporting currency value of the cost disposed from the asset.  """  
      self.DocProceed:int = obj["DocProceed"]
      """  The sales amount of the disposal in the currency specified.  """  
      self.Rpt1Proceed:int = obj["Rpt1Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt2Proceed:int = obj["Rpt2Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.Rpt3Proceed:int = obj["Rpt3Proceed"]
      """  Reporting currency value of the proceed cost from the asset.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.DocProceedInvBal:int = obj["DocProceedInvBal"]
      """  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.TransferBVFrom:str = obj["TransferBVFrom"]
      """  Determines Asset Register from which Book Value will be taken as Proceeds.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CustID:str = obj["CustID"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether the serial numbers are required in AssetDispEntry  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.PartLotTracked:bool = obj["PartLotTracked"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      self.WhseDescription:str = obj["WhseDescription"]
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

class Erp_Tablesets_UpdExtAssetDispEntryTableset:
   def __init__(self, obj):
      self.FADisposal:list[Erp_Tablesets_FADisposalRow] = obj["FADisposal"]
      self.FADisposalAttch:list[Erp_Tablesets_FADisposalAttchRow] = obj["FADisposalAttch"]
      self.FADispReg:list[Erp_Tablesets_FADispRegRow] = obj["FADispReg"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetNum
   disposalNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.disposalNum:int = obj["disposalNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetDispEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetDispEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetDispEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FADisposalListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFADispReg_input:
   """ Required : 
   ds
   assetNum
   disposalNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.disposalNum:int = obj["disposalNum"]
      pass

class GetNewFADispReg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFADisposalAttch_input:
   """ Required : 
   ds
   assetNum
   disposalNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.disposalNum:int = obj["disposalNum"]
      pass

class GetNewFADisposalAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFADisposal_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFADisposal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFADisposal
   whereClauseFADisposalAttch
   whereClauseFADispReg
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFADisposal:str = obj["whereClauseFADisposal"]
      self.whereClauseFADisposalAttch:str = obj["whereClauseFADisposalAttch"]
      self.whereClauseFADispReg:str = obj["whereClauseFADispReg"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetDispEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   company
   assetNum
   disposalNum
   ds
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The Asset Number  """  
      self.assetNum:str = obj["assetNum"]
      """  The Asset Number  """  
      self.disposalNum:int = obj["disposalNum"]
      """  The Disposal number  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
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

class LeaveBinNum_input:
   """ Required : 
   ipBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipBinNum:str = obj["ipBinNum"]
      """  bin that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveCustID_input:
   """ Required : 
   ipcustid
   ds
   """  
   def __init__(self, obj):
      self.ipcustid:str = obj["ipcustid"]
      """  custid that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveDisposalCost_input:
   """ Required : 
   ipdisposalcost
   ds
   """  
   def __init__(self, obj):
      self.ipdisposalcost:int = obj["ipdisposalcost"]
      """  disposalcost that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveDisposalCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveDisposalType_input:
   """ Required : 
   ipdisposaltype
   ds
   """  
   def __init__(self, obj):
      self.ipdisposaltype:str = obj["ipdisposaltype"]
      """  disposal type that was selected.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveDisposalType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveDisposed_input:
   """ Required : 
   ipDisposed
   ds
   """  
   def __init__(self, obj):
      self.ipDisposed:str = obj["ipDisposed"]
      """  Disposal Date that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveDisposed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveJobNum_input:
   """ Required : 
   ipjobnum
   ds
   """  
   def __init__(self, obj):
      self.ipjobnum:str = obj["ipjobnum"]
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveOrderNum_input:
   """ Required : 
   ipordernum
   ds
   """  
   def __init__(self, obj):
      self.ipordernum:int = obj["ipordernum"]
      """  ordernum that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeavePartNum_input:
   """ Required : 
   ippartnum
   ds
   """  
   def __init__(self, obj):
      self.ippartnum:str = obj["ippartnum"]
      """  partnum that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeavePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveProceed_input:
   """ Required : 
   ipproceed
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipproceed:int = obj["ipproceed"]
      """  disposalcost that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveProceed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveWarehouseCode_input:
   """ Required : 
   ipWarehouseCode
   ds
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  warehouse code that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class LeaveWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnSetReadyToPost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class OnSetReadyToPost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetDispEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetDispEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetDispEntryTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

