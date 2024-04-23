import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DigitalCertificateStoreSvc
# Description: DigitalCertificateStoreSvc BO for store certificates in DB
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DigitalCertificateStores(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DigitalCertificateStores items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DigitalCertificateStores
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DigitalCertificateStoreRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/DigitalCertificateStores",headers=creds) as resp:
           return await resp.json()

async def post_DigitalCertificateStores(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DigitalCertificateStores
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DigitalCertificateStoreRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DigitalCertificateStoreRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/DigitalCertificateStores", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DigitalCertificateStores_Company_CertificateID(Company, CertificateID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DigitalCertificateStore item
   Description: Calls GetByID to retrieve the DigitalCertificateStore item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DigitalCertificateStore
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateID: Desc: CertificateID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DigitalCertificateStoreRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/DigitalCertificateStores(" + Company + "," + CertificateID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DigitalCertificateStores_Company_CertificateID(Company, CertificateID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DigitalCertificateStore for the service
   Description: Calls UpdateExt to update DigitalCertificateStore. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DigitalCertificateStore
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateID: Desc: CertificateID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DigitalCertificateStoreRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/DigitalCertificateStores(" + Company + "," + CertificateID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DigitalCertificateStores_Company_CertificateID(Company, CertificateID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DigitalCertificateStore item
   Description: Call UpdateExt to delete DigitalCertificateStore item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DigitalCertificateStore
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateID: Desc: CertificateID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/DigitalCertificateStores(" + Company + "," + CertificateID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DigitalCertificateStoreListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDigitalCertificateStore, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseDigitalCertificateStore=" + whereClauseDigitalCertificateStore
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(certificateID, epicorHeaders = None):
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
   params += "certificateID=" + certificateID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddOrUpdateDigitalCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddOrUpdateDigitalCertificate
   Description: Saving certificate in store
   OperationID: AddOrUpdateDigitalCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddOrUpdateDigitalCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddOrUpdateDigitalCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCertificateStoreByThumbprint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCertificateStoreByThumbprint
   Description: Get Digital Certificate by using Thumbprint
   OperationID: GetCertificateStoreByThumbprint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCertificateStoreByThumbprint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCertificateStoreByThumbprint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCertificateStoreByIssuer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCertificateStoreByIssuer
   Description: Get Digital Certificate by using Issuer
   OperationID: GetCertificateStoreByIssuer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCertificateStoreByIssuer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCertificateStoreByIssuer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetThumbprintByFriendlyName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetThumbprintByFriendlyName
   Description: Gets thumprint of stored certificate by its friendly name
   OperationID: GetThumbprintByFriendlyName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetThumbprintByFriendlyName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetThumbprintByFriendlyName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddCertificate
   Description: Stores Certificate in Database
   OperationID: AddCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyToCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyToCompany
   Description: Copy (with replacing) certificate to other company
This function is used for CSF Netherlands
   OperationID: CopyToCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyToCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyToCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSelfSignedCertificateNSaveToServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSelfSignedCertificateNSaveToServer
   Description: Create self-signed certificate, add it to the list and export .cer file.
   OperationID: GenerateSelfSignedCertificateNSaveToServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSelfSignedCertificateNSaveToServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSelfSignedCertificateNSaveToServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSelfSignedCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSelfSignedCertificate
   Description: Create self-signed certificate, add it to the list and export .cer file.
   OperationID: GenerateSelfSignedCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSelfSignedCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSelfSignedCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasPrivateKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasPrivateKey
   Description: Check the Certificate File has private key
   OperationID: HasPrivateKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasPrivateKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasPrivateKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDigitalCertificateStore(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDigitalCertificateStore
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDigitalCertificateStore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDigitalCertificateStore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDigitalCertificateStore_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DigitalCertificateStoreSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DigitalCertificateStoreListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DigitalCertificateStoreListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DigitalCertificateStoreRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DigitalCertificateStoreRow] = obj["value"]
      pass

class Ice_Tablesets_DigitalCertificateStoreListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.CryptographyType:str = obj["CryptographyType"]
      """  CryptographyType  """  
      self.ThumbPrint:str = obj["ThumbPrint"]
      """  ThumbPrint  """  
      self.Issuer:str = obj["Issuer"]
      """  Issuer  """  
      self.Subject:str = obj["Subject"]
      """  Subject  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ExpiredOn:str = obj["ExpiredOn"]
      """  ExpiredOn  """  
      self.ValidOn:str = obj["ValidOn"]
      """  ValidOn  """  
      self.CertificateContent:str = obj["CertificateContent"]
      """  CertificateContent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DigitalCertificateStoreRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.CryptographyType:str = obj["CryptographyType"]
      """  CryptographyType  """  
      self.ThumbPrint:str = obj["ThumbPrint"]
      """  ThumbPrint  """  
      self.Issuer:str = obj["Issuer"]
      """  Issuer  """  
      self.Subject:str = obj["Subject"]
      """  Subject  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ExpiredOn:str = obj["ExpiredOn"]
      """  ExpiredOn  """  
      self.ValidOn:str = obj["ValidOn"]
      """  ValidOn  """  
      self.CertificateContent:str = obj["CertificateContent"]
      """  CertificateContent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  Company Visibility Flag  """  
      self.KeyID:str = obj["KeyID"]
      """  Temporary CertificateID  """  
      self.KeyPassword:str = obj["KeyPassword"]
      """  Certificate Key Password  """  
      self.PrivateKey:str = obj["PrivateKey"]
      """  Certificate Private Key  """  
      self.PublicKey:str = obj["PublicKey"]
      """  Certificate Public Key  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddCertificate_input:
   """ Required : 
   certByte
   """  
   def __init__(self, obj):
      self.certByte:str = obj["certByte"]
      """  X509certificate to store  """  
      pass

class AddCertificate_output:
   def __init__(self, obj):
      pass

class AddOrUpdateDigitalCertificate_input:
   """ Required : 
   sID
   sPublicKey
   sPrivateKey
   sKeyPassword
   """  
   def __init__(self, obj):
      self.sID:str = obj["sID"]
      self.sPublicKey:str = obj["sPublicKey"]
      self.sPrivateKey:str = obj["sPrivateKey"]
      self.sKeyPassword:str = obj["sKeyPassword"]
      pass

class AddOrUpdateDigitalCertificate_output:
   def __init__(self, obj):
      pass

class CopyToCompany_input:
   """ Required : 
   certByte
   toCompanyID
   """  
   def __init__(self, obj):
      self.certByte:str = obj["certByte"]
      """  certificate  """  
      self.toCompanyID:str = obj["toCompanyID"]
      """  CompanyID of destination  """  
      pass

class CopyToCompany_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   certificateID
   """  
   def __init__(self, obj):
      self.certificateID:str = obj["certificateID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GenerateSelfSignedCertificateNSaveToServer_input:
   """ Required : 
   certificateID
   validUntil
   """  
   def __init__(self, obj):
      self.certificateID:str = obj["certificateID"]
      """  Certificate ID to use as CN and friendly name.  """  
      self.validUntil:str = obj["validUntil"]
      """  Utc Date time until certificate is valid.  """  
      pass

class GenerateSelfSignedCertificateNSaveToServer_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Server path where the certificate is saved  """  
      pass

class GenerateSelfSignedCertificate_input:
   """ Required : 
   certificateID
   validUntil
   """  
   def __init__(self, obj):
      self.certificateID:str = obj["certificateID"]
      """  Certificate ID to use as CN and friendly name.  """  
      self.validUntil:str = obj["validUntil"]
      """  Utc Date time until certificate is valid.  """  
      pass

class GenerateSelfSignedCertificate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Exported certificate bytes.  """  
      pass

class GetByID_input:
   """ Required : 
   certificateID
   """  
   def __init__(self, obj):
      self.certificateID:str = obj["certificateID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["returnObj"]
      pass

class GetCertificateStoreByIssuer_input:
   """ Required : 
   issuer
   """  
   def __init__(self, obj):
      self.issuer:str = obj["issuer"]
      pass

class GetCertificateStoreByIssuer_output:
   def __init__(self, obj):
      self.returnObj:list[System_Security_Cryptography_X509Certificates_X509Certificate2] = obj["returnObj"]
      pass

class GetCertificateStoreByThumbprint_input:
   """ Required : 
   thumbprint
   """  
   def __init__(self, obj):
      self.thumbprint:str = obj["thumbprint"]
      pass

class GetCertificateStoreByThumbprint_output:
   def __init__(self, obj):
      self.returnObj:list[System_Security_Cryptography_X509Certificates_X509Certificate2] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DigitalCertificateStoreListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDigitalCertificateStore_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["ds"]
      pass

class GetNewDigitalCertificateStore_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDigitalCertificateStore
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDigitalCertificateStore:str = obj["whereClauseDigitalCertificateStore"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetThumbprintByFriendlyName_input:
   """ Required : 
   friendlyName
   """  
   def __init__(self, obj):
      self.friendlyName:str = obj["friendlyName"]
      """  Friendly name of certificate  """  
      pass

class GetThumbprintByFriendlyName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Thumprint of stored certificate by its friendly name or string.Empty  """  
      pass

class HasPrivateKey_input:
   """ Required : 
   sPublicKeyFilename
   """  
   def __init__(self, obj):
      self.sPublicKeyFilename:str = obj["sPublicKeyFilename"]
      """  Public Key File Name  """  
      pass

class HasPrivateKey_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Return true if it has a private key or else return false  """  
      pass

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

class Ice_Tablesets_DigitalCertificateStoreListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.CryptographyType:str = obj["CryptographyType"]
      """  CryptographyType  """  
      self.ThumbPrint:str = obj["ThumbPrint"]
      """  ThumbPrint  """  
      self.Issuer:str = obj["Issuer"]
      """  Issuer  """  
      self.Subject:str = obj["Subject"]
      """  Subject  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ExpiredOn:str = obj["ExpiredOn"]
      """  ExpiredOn  """  
      self.ValidOn:str = obj["ValidOn"]
      """  ValidOn  """  
      self.CertificateContent:str = obj["CertificateContent"]
      """  CertificateContent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DigitalCertificateStoreListTableset:
   def __init__(self, obj):
      self.DigitalCertificateStoreList:list[Ice_Tablesets_DigitalCertificateStoreListRow] = obj["DigitalCertificateStoreList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DigitalCertificateStoreRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.CryptographyType:str = obj["CryptographyType"]
      """  CryptographyType  """  
      self.ThumbPrint:str = obj["ThumbPrint"]
      """  ThumbPrint  """  
      self.Issuer:str = obj["Issuer"]
      """  Issuer  """  
      self.Subject:str = obj["Subject"]
      """  Subject  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ExpiredOn:str = obj["ExpiredOn"]
      """  ExpiredOn  """  
      self.ValidOn:str = obj["ValidOn"]
      """  ValidOn  """  
      self.CertificateContent:str = obj["CertificateContent"]
      """  CertificateContent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  Company Visibility Flag  """  
      self.KeyID:str = obj["KeyID"]
      """  Temporary CertificateID  """  
      self.KeyPassword:str = obj["KeyPassword"]
      """  Certificate Key Password  """  
      self.PrivateKey:str = obj["PrivateKey"]
      """  Certificate Private Key  """  
      self.PublicKey:str = obj["PublicKey"]
      """  Certificate Public Key  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DigitalCertificateStoreTableset:
   def __init__(self, obj):
      self.DigitalCertificateStore:list[Ice_Tablesets_DigitalCertificateStoreRow] = obj["DigitalCertificateStore"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtDigitalCertificateStoreTableset:
   def __init__(self, obj):
      self.DigitalCertificateStore:list[Ice_Tablesets_DigitalCertificateStoreRow] = obj["DigitalCertificateStore"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class System_Security_Cryptography_AsnEncodedData:
   def __init__(self, obj):
      self.Oid:list[System_Security_Cryptography_Oid] = obj["Oid"]
      self.RawData:str = obj["RawData"]
      pass

class System_Security_Cryptography_AsymmetricAlgorithm:
   def __init__(self, obj):
      self.KeySize:int = obj["KeySize"]
      self.LegalKeySizes:list[System_Security_Cryptography_KeySizes] = obj["LegalKeySizes"]
      self.SignatureAlgorithm:str = obj["SignatureAlgorithm"]
      self.KeyExchangeAlgorithm:str = obj["KeyExchangeAlgorithm"]
      pass

class System_Security_Cryptography_KeySizes:
   def __init__(self, obj):
      self.MinSize:int = obj["MinSize"]
      self.MaxSize:int = obj["MaxSize"]
      self.SkipSize:int = obj["SkipSize"]
      pass

class System_Security_Cryptography_Oid:
   def __init__(self, obj):
      self.Value:str = obj["Value"]
      self.FriendlyName:str = obj["FriendlyName"]
      pass

class System_Security_Cryptography_X509Certificates_PublicKey:
   def __init__(self, obj):
      self.EncodedKeyValue:list[System_Security_Cryptography_AsnEncodedData] = obj["EncodedKeyValue"]
      self.EncodedParameters:list[System_Security_Cryptography_AsnEncodedData] = obj["EncodedParameters"]
      self.Key:list[System_Security_Cryptography_AsymmetricAlgorithm] = obj["Key"]
      self.Oid:list[System_Security_Cryptography_Oid] = obj["Oid"]
      pass

class System_Security_Cryptography_X509Certificates_X500DistinguishedName:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Oid:list[System_Security_Cryptography_Oid] = obj["Oid"]
      self.RawData:str = obj["RawData"]
      pass

class System_Security_Cryptography_X509Certificates_X509Certificate2:
   def __init__(self, obj):
      self.Archived:bool = obj["Archived"]
      self.Extensions:list[System_Security_Cryptography_X509Certificates_X509Extension] = obj["Extensions"]
      self.FriendlyName:str = obj["FriendlyName"]
      self.HasPrivateKey:bool = obj["HasPrivateKey"]
      self.PrivateKey:list[System_Security_Cryptography_AsymmetricAlgorithm] = obj["PrivateKey"]
      self.IssuerName:list[System_Security_Cryptography_X509Certificates_X500DistinguishedName] = obj["IssuerName"]
      self.NotAfter:str = obj["NotAfter"]
      self.NotBefore:str = obj["NotBefore"]
      self.PublicKey:list[System_Security_Cryptography_X509Certificates_PublicKey] = obj["PublicKey"]
      self.RawData:str = obj["RawData"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.SignatureAlgorithm:list[System_Security_Cryptography_Oid] = obj["SignatureAlgorithm"]
      self.SubjectName:list[System_Security_Cryptography_X509Certificates_X500DistinguishedName] = obj["SubjectName"]
      self.Thumbprint:str = obj["Thumbprint"]
      self.Version:int = obj["Version"]
      self.Handle      #schema had no properties on an object.
      self.Issuer:str = obj["Issuer"]
      self.Subject:str = obj["Subject"]
      pass

class System_Security_Cryptography_X509Certificates_X509Extension:
   def __init__(self, obj):
      self.Critical:bool = obj["Critical"]
      self.Oid:list[System_Security_Cryptography_Oid] = obj["Oid"]
      self.RawData:str = obj["RawData"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDigitalCertificateStoreTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDigitalCertificateStoreTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DigitalCertificateStoreTableset] = obj["ds"]
      pass

      """  output parameters  """  

