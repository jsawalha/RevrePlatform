/*
 * Swagger propertiestore
 *
 * This is a sample propertiestore server.  You can find  out more about Swagger at  [http://swagger.io](http://swagger.io) or on  [irc.freenode.net, #swagger](http://swagger.io/irc/). 
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

type Address struct {

	StreetAddress string `json:"StreetAddress,omitempty"`

	StreetNumber int32 `json:"StreetNumber,omitempty"`

	StreetNanme string `json:"StreetNanme,omitempty"`

	City string `json:"City,omitempty"`

	Province string `json:"Province,omitempty"`

	PostalCode string `json:"PostalCode,omitempty"`

	Country string `json:"Country,omitempty"`
}